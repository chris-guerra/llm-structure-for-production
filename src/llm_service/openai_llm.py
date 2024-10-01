"""
LLM Script Oriented to using OpenAI structure
"""

from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

# Initialize LLM
MODEL = 'gpt-4o-mini'
llm = ChatOpenAI(model_name= MODEL, temperature= 0)

examples = [
    {"color": "red", "emotion": "passion"},
    {"color": "blue", "emotion": "serenity"},
    {"color": "green", "emotion": "tranquility"},
]

example_formatter_template = """
Color: {color}
Emotion: {emotion}
"""

example_prompt = PromptTemplate(
    input_variables=["color", "emotion"],
    template=example_formatter_template,
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="""Here are some examples of colors and the emotions associated with \
them:""",
    suffix="""Now, given a new color, identify the emotion associated with \
it:\nColor: {input}\nEmotion:""",
    input_variables=["input"],
    example_separator="\n",
)

formatted_prompt = few_shot_prompt.format(input="purple")
prompt=PromptTemplate(template=formatted_prompt, input_variables=[])

# Create the LLMChain for the prompt
chain = prompt | llm

# Run the LLMChain to get the AI-generated emotion associated with the input
# color
response = chain.invoke({})

# We print the example of the prompt sent
print("Input: 'Color: purple'")
print("Output: 'Emotion:", f"{response.content}'")
print(f"\nPrompt:\n\n{prompt.template}")
