from huggingface_hub import InferenceClient

client = InferenceClient(
	provider="replicate",
	api_key="Token_Place"
)
prompt = str(input("add your prompt: "))

image = client.text_to_image(
	prompt,
	model="black-forest-labs/FLUX.1-schnell"
)
image.save("gen.png", scale=20)