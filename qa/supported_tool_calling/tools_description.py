# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 17:35
# @Author  : nongbin
# @FileName: tools_description.py
# @Software: PyCharm
# @Affiliation: tfswufe.edu.cn

GET_PERSONAL_PROFILE = {
    "type": "function",
    "function": {
        "name": "get_personal_profile",
        "description": "根据人的姓名，介绍这个人的基本信息",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "人的姓名",
                },
            }
        },
        "required": ["name"]
    }
}

GET_RELATION_INFO = {
    "type": "function",
    "function": {
        "name": "get_relation_info",
        "description": "给定两个诗人的姓名，查询两个人的关系, 比如李白与杜甫的关系是什么",
        "parameters": {
            "type": "object",
            "properties": {
                "first_entity_name": {
                    "type": "string",
                    "description": "第一个人的姓名",
                },
                "second_entity_name": {
                    "type": "string",
                    "description": "第二个人的姓名",
                }
            }
        }
    }
}

GET_HELLO_INFO = {
    "type": "function",
    "function": {
        "name": "get_hello_info",
        "description": "回应用户的问候，比如，用户问候“您好”，就要调用这个工具",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "用户问候的内容",
                }
            }
        }
    }
}

GENERATE_IMAGES = {
    "type": "function",
    "function": {
        "name": "generate_images",
        "description": "根据用户的描述，生成图片",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "用户的描述",
                }
            }
        }
    }
}

GENERATE_SPEECH = {
    "type": "function",
    "function": {
        "name": "generate_speech",
        "description": "根据用户的描述，生成语音",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "用户的描述",
                },
                "language": {
                    "type": "string",
                    "description": "语音的语言",
                    "enum": ["陕西话", "东北话", "粤语"]
                },
                "gender": {
                    "type": "string",
                    "description": "语音的性别",
                    "enum": ["男声", "女声"]
                }
            },
            "required": ["text"]
        }
    }
}
CLONE_VOICE = {
    "type": "function",
    "function": {
        "name": "clone_voice",
        "description": "根据提供克隆或者模仿声音对象的姓名，克隆语音，例如‘请用张三的声音朗读一下这首诗’",
        "parameters": {
            "type": "object",
            "properties": {
                "text_to_gen": {
                    "type": "string",
                    "description": "语音脚本文字",
                },
                "reference_audio": {
                    "type": "string",
                    "description": "参考克隆声音对象的姓名或者称呼",
                }
            }
        }
    }
}
GENERATE_VIDEO = {
    "type": "function",
    "function": {
        "name": "generate_video",
        "description": "根据用户的描述，生成视频",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "用户的描述",
                }
            }
        }
    }
}
GENERATE_DIGITAL_MEN = {
    "type": "function",
    "function": {
        "name": "generate_digital_men",
        "description": "根据用户的要求，生成数字人",
        "parameters": {
            "type": "object",
            "properties": {
                "transcript": {
                    "type": "string",
                    "description": "数字人播报的内容",
                }
            }
        }
    }
}
SEARCH_DOCUMENTS = {
    "type": "function",
    "function": {
        "name": "search_documents",
        "description": "根据用户文献检索要求，检索相应的文献，并回答问题",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "用户的描述",
                }
            }
        }
    }
}
GENERATE_PPT = {
    "type": "function",
    "function": {
        "name": "generate_ppt",
        "description": "根据用户的要求，生成PPT演示文档",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "用户的描述",
                }
            }
        }
    }
}
SEARCH_POETRY_BY_CHINESE = {
    "type": "function",
    "function": {
        "name": "search_poetry_by_chinese",
        "description": "根据提供的白话文或者现代文，搜索古文",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "用户提供的内容",
                }
            }
        }
    }
}
SEARCH_POETRY_BY_POETRY = {
    "type": "function",
    "function": {
        "name": "search_poetry_by_poetry",
        "description": "根据提供的古文搜索古文",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "用户提供的内容",
                }
            }
        }
    }
}
