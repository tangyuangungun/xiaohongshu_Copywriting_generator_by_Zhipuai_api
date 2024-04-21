from prompt_template import system_template_text
from zhipuai import ZhipuAI
from configparser import ConfigParser

# 创建 ConfigParser 对象
config = ConfigParser()

# 读取配置文件
config.read('config.ini')

# 获取 API 密钥
API_key = ZhipuAI(api_key=config['DEFAULT']['API_KEY'])

def generate_xiaohongshu(theme):
    response_result = API_key.chat.completions.create(
        model="glm-3-turbo",  # 填写需要调用的模型名称
        messages=[
            {"role": "system", "content": system_template_text},
            {"role": "user", "content": theme}
        ],)
    result = response_result.choices[0].message.content
    return result




    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", system_template_text),
    #     ("user", user_template_text)
    # ])
    # model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)
    # output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    # chain = prompt | model | output_parser
    # result = chain.invoke({
    #     "parser_instructions": output_parser.get_format_instructions(),
    #     "theme": theme
    # })
    # return result

# print(generate_xiaohongshu("大模型"))

