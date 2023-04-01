import openai
import config
import typer
from rich import print
from rich.table import Table



def __prompt() -> str:
    """ Esta funcion pide un prompt y evalua si el usuario desea salir ('exit') o crear un nuevo contexto de conversacion ('new') """

     # Prompt
    prompt = typer.prompt("\nDe que queres hablar")

    if prompt == "exit":
        exit = typer.confirm("¿Estas seguro?")
        if exit:
            print("Nos vemos la proxima crack")
            raise typer.Abort()
        return __prompt()
                
    return prompt

def main():
    """ Esta funcion es la principal que ejecuta mi programa y posee un iterador while para entablar conversaciones con chatGpt """

    # Saludo inicial
    print("\n[bold green4 u]Aplicacion de consola que utiliza la API de chatGpt [bold blue u](en Python)[bold blue u][/bold green4 u]\n")

    # Tabla
    table = Table("Comando", "Descripcion")
    table.add_row("[green4]new[/green4]", "crear una nueva conversacion")
    table.add_row("[red]exit[red]", "salir de la aplicacion")
    print(table)

    # Configuraciond e API_KEY
    openai.api_key = config.api_key

    # Inicio una lista de diccionarios donde la clave "role": "system" genera  el contexto que se le da al asistente
    context = {"role":"system", "content":"charlas filosoficas, de sistemas informaticos y por supuesto de la vida misma"}
    messages = [context]

    # Comienza el bucle para armar la conversacion
    while True:


        # Prompt
        prompt = __prompt()

        if prompt == "new":
            newContext = typer.prompt("\nIngrese el contexto de la nueva conversacion (rol del asistente)")
            context = {"role":"system", "content":newContext}
            print("Nueva conversacion creada")
            messages = [context]
            prompt = __prompt()
    

        # Guardo el prompt del usuario en la lista iniciada anteriormente
        messages.append({"role": "user", "content": prompt})

        # Recibo la respuesta completa
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=3800)

        # Separo el contenido que me interesa de la respuesta
        responseContent = response.choices[0].message.content

        # Guardo la respuesta del asistente en la lista iniciada anteriormente
        messages.append({"role": "assistant", "content": responseContent})

        # Imprimo respuesta 
        print(f"\n[bold green4]> {responseContent}[/bold green4]")


# Esto es parte de typer para "hacer la app de consola"
if __name__ == "__main__":
    typer.run(main)

