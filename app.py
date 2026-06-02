from pathlib import Path
from tkinter import Tk, filedialog, messagebox
from nfelib.nfe.bindings.v4_0.proc_nfe_v4_00 import NfeProc

def gerar_danfe():
    caminho_xml = filedialog.askopenfilename(
        title="Selecione o XML da NF-e",
        filetypes=[("Arquivos XML", "*.xml")]
    )

    if not caminho_xml:
        return

    try:
        xml_path = Path(caminho_xml)

        with open(xml_path, "r", encoding="utf-8") as arquivo:
            xml = arquivo.read()

        nfe = NfeProc.from_xml(xml)

        pdf_bytes = nfe.to_pdf()

        caminho_pdf = filedialog.asksaveasfilename(
            title="Salvar DANFE em PDF",
            defaultextension=".pdf",
            initialfile=f"{xml_path.stem}.pdf",
            filetypes=[("PDF", "*.pdf")]
        )

        if not caminho_pdf:
            return

        with open(caminho_pdf, "wb") as pdf:
            pdf.write(pdf_bytes)

        messagebox.showinfo("Sucesso", "DANFE gerada em PDF com sucesso!")

    except Exception as erro:
        messagebox.showerror("Erro", f"Não foi possível gerar a DANFE:\n\n{erro}")

janela = Tk()
janela.title("Gerador de DANFE")
janela.geometry("300x150")

botao = __import__("tkinter").Button(
    janela,
    text="Selecionar XML e gerar DANFE",
    command=gerar_danfe,
    width=30,
    height=2
)
botao.pack(pady=40)

janela.mainloop()