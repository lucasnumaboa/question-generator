import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import os
from pathlib import Path


class QuizHTMLGenerator(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")  # Você pode escolher outros temas disponíveis
        self.title("Gerador de Questionários HTML")
        self.geometry("800x800")  # Ajuste a altura conforme necessário

        # Instruções
        instruction = ttk.Label(
            self,
            text=(
                "Cole as informações no formato abaixo (cada campo separado por ponto e vírgula ';'):\n"
                "pergunta ; resposta 1 ; resposta 2 ; ... ; resposta N ; gabarito\n"
                "Onde N é a quantidade de alternativas escolhida (máximo 6)."
            ),
            bootstyle="info",
            wraplength=760,
            justify="left"
        )
        instruction.pack(pady=10, padx=20)

        # Caixa de texto para entrada
        self.text_box = ttk.Text(self, wrap="word", height=30)
        self.text_box.pack(expand=True, fill='both', padx=20, pady=10)

        # Frame para entradas adicionais
        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(pady=10, padx=20, fill='x')

        # Frame interno para nome do arquivo
        file_frame = ttk.Frame(bottom_frame)
        file_frame.pack(side='top', fill='x', pady=(0, 5))

        # Label e entrada para o nome do arquivo
        filename_label = ttk.Label(file_frame, text="Nome do arquivo:")
        filename_label.pack(side='left', padx=(0, 5))

        self.filename_entry = ttk.Entry(file_frame)
        self.filename_entry.pack(side='left', expand=True, fill='x', padx=(0, 5))
        self.filename_entry.insert(0, "questionario")  # Nome padrão

        # Frame interno para o título
        title_frame = ttk.Frame(bottom_frame)
        title_frame.pack(side='top', fill='x', pady=(0, 5))

        # Label e entrada para o título do HTML
        title_label = ttk.Label(title_frame, text="Título do HTML:")
        title_label.pack(side='left', padx=(0, 5))

        self.title_entry = ttk.Entry(title_frame)
        self.title_entry.pack(side='left', expand=True, fill='x', padx=(0, 5))
        self.title_entry.insert(0, "Título do cabeçalho web")  # Título padrão

        # Frame interno para a quantidade de alternativas
        options_frame = ttk.Frame(bottom_frame)
        options_frame.pack(side='top', fill='x', pady=(0, 5))

        # Label e Spinbox para a quantidade de alternativas
        options_label = ttk.Label(options_frame, text="Quantidade de Alternativas:")
        options_label.pack(side='left', padx=(0, 5))

        self.options_spinbox = ttk.Spinbox(
            options_frame,
            from_=2,
            to=6,
            width=5,
            state='readonly'
        )
        self.options_spinbox.pack(side='left', padx=(0, 5))
        self.options_spinbox.set(5)  # Valor padrão

        # Botão para gerar o HTML
        generate_button = ttk.Button(bottom_frame, text="Gerar HTML", command=self.generate_html, bootstyle="success")
        generate_button.pack(side='left', pady=(10, 0))

    def generate_html(self):
        input_text = self.text_box.get("1.0", "end").strip()
        filename = self.filename_entry.get().strip()
        title = self.title_entry.get().strip()
        num_options = self.options_spinbox.get().strip()

        # Validação de entrada
        if not filename:
            messagebox.showerror("Erro", "Por favor, insira um nome para o arquivo.")
            return

        if not title:
            messagebox.showerror("Erro", "Por favor, insira um título para o HTML.")
            return

        try:
            num_options = int(num_options)
            if not (2 <= num_options <= 6):
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Quantidade de alternativas deve ser um número entre 2 e 6.")
            return

        lines = input_text.splitlines()
        questions = []
        correct_answers = {}
        question_number = 1

        for line_num, line in enumerate(lines, start=1):
            parts = [part.strip() for part in line.split(';')]
            expected_parts = num_options + 2  # pergunta + respostas + gabarito
            if len(parts) != expected_parts:
                messagebox.showerror(
                    "Erro de Formato",
                    f"Linha {line_num} deve ter {expected_parts} partes separadas por ponto e vírgula ';'.\n"
                    f"Encontrado: {len(parts)} partes."
                )
                return
            question = parts[0]
            answers = parts[1:num_options + 1]
            gabarito = parts[-1].lower()

            # Validar gabarito
            valid_options = [chr(97 + i) for i in range(num_options)]  # ['a', 'b', ..., up to num_options]
            if gabarito not in valid_options:
                messagebox.showerror(
                    "Erro de Gabarito",
                    f"Gabarito inválido na linha {line_num}. Deve ser uma das opções: {', '.join(valid_options)}."
                )
                return

            questions.append({
                'number': question_number,
                'question': question,
                'answers': answers,
            })
            correct_answers[str(question_number)] = gabarito
            question_number += 1

        # Construção do conteúdo HTML
        html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        .question {{
            margin-bottom: 20px;
        }}
        .option {{
            display: block;
            margin: 5px 0;
            padding: 10px;
            border: 1px solid #ccc;
            cursor: pointer;
        }}
        .option.correct {{
            background-color: lightgreen;
            border-color: green;
        }}
        .option.incorrect {{
            background-color: lightcoral;
            border-color: red;
        }}
        .result {{
            font-weight: bold;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div id="quiz">
"""

        for q in questions:
            html_content += f'        <div class="question">\n'
            html_content += f'            <p>{q["number"]}. {q["question"]}</p>\n'
            options = [chr(97 + i) for i in range(num_options)]  # ['a', 'b', ...]
            for i, answer in enumerate(q["answers"]):
                option = options[i]
                html_content += f'            <div class="option" data-question="{q["number"]}" data-answer="{option}">{option}) {answer}</div>\n'
            html_content += f'        </div>\n'

        html_content += f"""    </div>
    <div id="result" class="result"></div>
    <script>
        const correctAnswers = {{"""

        # Adiciona as respostas corretas
        correct_ans_list = [f'            {k}: "{v}"' for k, v in correct_answers.items()]
        html_content += ",\n".join(correct_ans_list)
        html_content += """
        };
        document.querySelectorAll('.option').forEach(option => {
            option.addEventListener('click', function() {
                const question = this.getAttribute('data-question');
                const answer = this.getAttribute('data-answer');
                const correct = correctAnswers[question];
                if (answer === correct) {
                    this.classList.add('correct');
                } else {
                    this.classList.add('incorrect');
                }
                document.querySelectorAll(`.option[data-question="${question}"]`).forEach(opt => {
                    opt.classList.add('disabled');
                    opt.style.pointerEvents = 'none';
                });
            });
        });

        function calculateScore() {
            let score = 0;
            document.querySelectorAll('.option.correct').forEach(option => {
                score++;
            });
            return score;
        }

        function displayResult() {
            const score = calculateScore();
            const totalQuestions = Object.keys(correctAnswers).length;
            const resultDiv = document.getElementById('result');
            resultDiv.textContent = `Você acertou ${score} de ${totalQuestions} questões.`;
        }

        document.getElementById('quiz').addEventListener('click', function() {
            displayResult();
        });
    </script>
</body>
</html>"""

        # Caminho para a área de trabalho
        desktop_path = Path.home() / 'Desktop'
        file_path = desktop_path / f"{filename}.html"

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            messagebox.showinfo("Sucesso", f"Arquivo HTML criado com sucesso em:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o arquivo:\n{e}")


def main():
    app = QuizHTMLGenerator()
    app.mainloop()


if __name__ == "__main__":
    main()
