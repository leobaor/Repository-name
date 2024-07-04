import asyncio

async def chatllm_Resolver(_, info, message_usr):
    print(message_usr)
    try:
        await asyncio.sleep(1)  # Espera 1 segundo sin bloquear
        payload = {
            "success": True,
            "message_llm": "Respuesta procesada",
            "errors": None
        }
    except Exception as error:
        payload = {
            "success": False,
            "message_llm": "Respuesta no procesada",
            "errors": [str(error)]
        }
    print("Respuesta")
    return payload

# Assuming chatllm_Resolver is defined as in your snippet

async def main():
    result = await chatllm_Resolver(None, None, "Test message")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())