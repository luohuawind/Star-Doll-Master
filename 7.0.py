import os
import pygame
import sys
import random  # 确保有这一行！
import math

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
SILVER = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 150, 255)
DARK_BLUE = (0, 0, 100)
GOLD = (255, 215, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BACKGROUND = (30, 30, 50)  # 深蓝色背景


# ========== 颜色定义 ==========
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
SILVER = (192, 192, 192)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 150, 255)
DARK_BLUE = (0, 0, 100)
GOLD = (255, 215, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)






BACKGROUND = (30, 30, 50)  # 深蓝色背景

fill_color = (255, 255, 255)  # 白色
fill_color = (0, 0, 0)        # 黑色
fill_color = (255, 0, 0)      # 红色


# ========== 颜色定义结束 ==========
# --- 专用字体定义 ---
pygame.font.init()

print("🎨 正在加载字体...")

# 游戏标题字体 - 华丽风格
try:
    game_title_font = pygame.font.Font("fonts/华文行楷.ttf", 60)
    print("✅ 游戏标题字体加载成功")
except:
    game_title_font = pygame.font.SysFont("simhei", 60, bold=True)  # 修正：simhei
    print("⚠️ 使用默认游戏标题字体")

# 屏幕标题字体 - 优雅风格
try:
    screen_title_font = pygame.font.Font("fonts/微软雅黑.ttf", 48)
    print("✅ 屏幕标题字体加载成功")
except:
    screen_title_font = pygame.font.SysFont("microsoftyahei", 48, bold=True)
    print("⚠️ 使用默认屏幕标题字体")

# 角色名字字体 - 醒目风格
try:
    character_name_font = pygame.font.Font("fonts/黑体.ttf", 40)
    print("✅ 角色名字字体加载成功")
except:
    character_name_font = pygame.font.SysFont("simhei", 40, bold=True)  # 修正：simhei
    print("⚠️ 使用默认角色名字字体")

# 等级显示字体 - 强调风格
grade_font = pygame.font.SysFont("simhei", 38, bold=True)  # 修正：simhei

# 描述文字字体 - 清晰风格
try:
    description_font = pygame.font.Font("fonts/宋体.ttf", 26)
    print("✅ 描述文字字体加载成功")
except:
    description_font = pygame.font.SysFont("simsun", 26)  # 修正：simsun
    print("⚠️ 使用默认描述文字字体")

# 按钮字体 - 简洁风格
button_font = pygame.font.SysFont("simhei", 24)  # 修正：simhei

# 提示文字字体 - 细小风格
try:
    hint_font = pygame.font.Font("fonts/楷体.ttf", 18)
    
    print("✅ 提示文字字体加载成功")
except:
    hint_font = pygame.font.SysFont("kaiti", 18)
    print("⚠️ 使用默认提示文字字体")

print("🎉 所有字体加载完成！")


# 初始化 Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800




# ========== Pygame 初始化 ==========
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("星际玩偶师")
clock = pygame.time.Clock()  # 时钟对象，用于控制帧率





# 直接指定桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
image_path = os.path.join(desktop_path, "0f1ffca2b27d35a0249f98925fe11152.jpg")

print(f"📁 桌面路径: {desktop_path}")
print(f"📁 图片路径: {image_path}")
print(f"📁 图片是否存在: {os.path.exists(image_path)}")

# 加载背景图片
try:
    # 直接指向你的桌面文件
    background_image = pygame.image.load(r"C:\Users\10653\Desktop\星际玩偶师\backgrounds\0f1ffca2b27d35a0249f98925fe11152.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    print("🎉 桌面背景图片加载成功！")
except Exception as e:
    background_image = None
    print(f"❌ 桌面背景图片加载失败: {e}")
    print("💡 请确认图片文件在桌面上且文件名正确")

# 颜色定义
BACKGROUND = (10, 10, 40)
# ... 其余代码


# 颜色定义
BACKGROUND = (10, 10, 40)
TEXT_COLOR = (255, 255, 255)
TITLE_COLOR = (255, 215, 0)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (100, 160, 210)
HIGHLIGHT_COLOR = (255, 105, 180)

# 字体设置
def get_chinese_font(size):
    chinese_fonts = ['simhei', 'microsoftyahei', 'msyh', 'simsun', 'Arial']
    for font_name in chinese_fonts:
        try:
            font = pygame.font.SysFont(font_name, size)
            test_surface = font.render('测试', True, (255, 255, 255))
            if test_surface.get_width() > 0:
                return font
        except:
            continue
    return pygame.font.Font(None, size)

title_font = get_chinese_font(48)
header_font = get_chinese_font(36)
normal_font = get_chinese_font(32)
small_font = get_chinese_font(28)

# 全局变量存储所有背景图
background_images = {}

import os

def load_background_image(image_name):
    """加载背景图片 - 在桌面星际玩偶师文件夹中查找"""
    if image_name in background_images:
        return background_images[image_name]
    
    try:
        # 获取桌面路径
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        # 你的游戏文件夹路径
        game_folder = os.path.join(desktop_path, "星际玩偶师")
        backgrounds_dir = os.path.join(game_folder, "backgrounds")
        
        print(f"🔍 查找路径: {backgrounds_dir}")  # 调试信息
        
        # 确保backgrounds文件夹存在
        if not os.path.exists(backgrounds_dir):
            print(f"❌ backgrounds文件夹不存在: {backgrounds_dir}")
            # 尝试直接在游戏文件夹查找文件
            image_path = os.path.join(game_folder, image_name)
        else:
            image_path = os.path.join(backgrounds_dir, image_name)
        
        print(f"🔍 尝试加载图片: {image_path}")  # 调试信息
        
        if os.path.exists(image_path):
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            background_images[image_name] = image
            print(f"✅ 背景图加载成功: {image_name}")
            return image
        else:
            print(f"❌ 图片文件不存在: {image_path}")
            # 尝试其他可能的路径
            return try_alternative_paths(image_name)
        
    except Exception as e:
        print(f"❌ 背景图加载异常 {image_name}: {e}")
        return None

def try_alternative_paths(image_name):
    """尝试其他可能的路径"""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    game_folder = os.path.join(desktop_path, "星际玩偶师")
    
    alternative_paths = [
        # 游戏文件夹的backgrounds文件夹
        os.path.join(game_folder, "backgrounds", image_name),
        # 游戏文件夹直接路径
        os.path.join(game_folder, image_name),
        # 桌面直接路径
        os.path.join(desktop_path, image_name),
        # 桌面backgrounds文件夹
        os.path.join(desktop_path, "backgrounds", image_name),
        # 当前目录
        image_name,
        # 当前目录的backgrounds文件夹
        os.path.join("backgrounds", image_name),
    ]
    
    for path in alternative_paths:
        try:
            if os.path.exists(path):
                print(f"✅ 在备用路径找到图片: {path}")
                image = pygame.image.load(path)
                image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
                background_images[image_name] = image
                return image
        except Exception as e:
            print(f"❌ 备用路径加载失败 {path}: {e}")
            continue
    
    print(f"❌ 所有路径都找不到图片: {image_name}")
    return None

def get_background_for_screen(screen_name, grade=None, race=None):
    """根据当前屏幕返回对应的背景图"""
    print(f"🔍 调试: screen_name={screen_name}, grade={grade}, race={race}")
    
    # 默认背景
    default_bg = None
    
    if screen_name == "welcome":
        # 欢迎界面背景
        bg = load_background_image("0f1ffca2b27d35a0249f98925fe11152.jpg")
        print(f"🎨 欢迎界面背景: {bg}")
        return bg or default_bg
        
    elif screen_name == "grade_selection":
        # 等级选择背景
        bg = load_background_image("1aa1bf749c794e806bdd3d25508547b3.jpg")
        print(f"🎨 等级选择背景: {bg}")
        return bg or default_bg
    
    elif screen_name == "race_selection":
        # 种族选择背景
        bg = load_background_image("e67189cd7c960bcd85a47cb1e6a62e26.jpg")
        print(f"🎨 种族选择背景: {bg}")
        return bg or default_bg
    
    elif screen_name == "character_display" and race:
        # 角色展示界面 - 使用角色专属背景
        try:
            print(f"🎯 尝试获取角色背景: grade={grade}, race={race}")
            
            if grade == "S":
                bg_name = characters_data["S"][race].get("background")
            elif grade in ["A", "E"]:
                bg_name = characters_data["A"][race].get("background") 
            elif grade in ["B", "C", "D"]:
                bg_name = characters_data["B"][race].get("background")
            else:  # F级
                bg_name = characters_data["F"][race].get("background")
            
            print(f"📁 背景文件名: {bg_name}")
            
            if bg_name:
                bg = load_background_image(bg_name)
                print(f"🎨 角色背景加载结果: {bg}")
                return bg or default_bg
        except Exception as e:
            print(f"❌ 获取角色背景出错: {e}")
            pass
    
    elif screen_name == "completion":
        bg = load_background_image("e8499f5305a217ff094d74ad5bb47a96.jpg")
        print(f"🎨 完成界面背景: {bg}")
        return bg or default_bg
    
    print(f"⚠️ 使用默认背景")
    return default_bg

def debug_file_locations():
    """调试文件位置信息"""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    game_folder = os.path.join(desktop_path, "星际玩偶师")
    backgrounds_dir = os.path.join(game_folder, "backgrounds")
    
    print(f"🏠 桌面路径: {desktop_path}")
    print(f"🎮 游戏文件夹: {game_folder}")
    print(f"🎨 背景文件夹: {backgrounds_dir}")
    
    # 检查游戏文件夹是否存在
    if os.path.exists(game_folder):
        print("✅ 游戏文件夹存在")
        # 检查backgrounds文件夹
        if os.path.exists(backgrounds_dir):
            print("✅ backgrounds文件夹存在")
            print("📁 backgrounds文件夹内容:")
            for file in os.listdir(backgrounds_dir):
                print(f"   - {file}")
        else:
            print("❌ backgrounds文件夹不存在")
    else:
        print("❌ 游戏文件夹不存在")

# 在程序开始时调用（可选）
debug_file_locations()



# 完整的角色数据
characters_data = {
    # S级角色 - 六个特殊角色
    "S": {
        "黑猫": {
            "name": "宋惊澜",
            "identity": "永生之地首席审讯官，少将军衔，负责看守与管理囚犯，以冷酷狠厉著称。",
            "appearance": "身材修长挺拔，军装严丝合缝，肩线平直，腰窄劲瘦，面容冷峻，眼神锐利如军刀，自带禁欲与压迫感。",
            "personality": "冷静精准，纪律严明，对外人冷漠无情，审讯手段狠辣；但对昼眠展现出矛盾的温柔与纵容，易被其捉弄，耳根易红，有'黑猫'般的傲娇与纯情。",
            "ability": "武力值高，擅长精神控制与审讯，精神体为通体漆黑的缅因猫（金色竖瞳），精神海为被荆棘与血月笼罩的哥特城堡。",
            "background": "c536c91b23fbe939aa2f977845356125.jpg"
        },
        "雪豹": {
            "name": "沈宴",
            "identity": "永生之地B栋唯一掌权者（老大），因权力斗争失败入狱，曾是星际贵族，以'风流倜傥、玩世不恭'闻名。",
            "appearance": "生得一副风流骨相，眉眼舒朗，眼尾微挑含笑意，鼻梁高挺，唇线分明，肤色白皙，穿剪裁精良的衣物，自带骄傲洒脱的贵族气质。",
            "personality": "表面阳光随和，实则暗藏上位者疏离；对昼眠极度执着（自称'老婆'），恋爱脑，易被昼眠的直球和玩笑逗笑或炸毛，本质单纯。",
            "ability": "精神体为被锁链束缚的雪豹（象征挣扎与野性），污染值曾达98，后因昼眠帮助降至安全值，擅长用魅力与手腕掌控B栋。",
            "background": "b83957d1a70e6eeef01708adbb2e85f6.jpg"
            
        },
        "耳廓狐": {
            "name": "苏不渡",
            "identity": "永生之地饭堂厨子，有隐藏身份，耳廓狐兽人，因未知原因被关押于此，是少数能制作真实食物（如蔬菜、兽肉）的人。",
            "appearance": "小麦色皮肤，鼻梁高挺，下颌线清晰，眼型偏圆、眼尾下垂，笑起来显稚气；金褐色瞳孔边缘有浅色光晕，头顶有淡金色耳廓狐大耳朵（耳尖深色、内侧粉白），银灰色短发凌乱，后脑勺有呆毛，尾毛蓬松。",
            "personality": "胆小敏感，初期因被欺凌而蜷缩，对昼眠有依赖与信任；善良细心，会关心昼眠饮食（如要求洗手），被触碰耳朵时会炸毛脸红，本质纯真，带着阳光烘烤过的暖意和恰到好处的粗粝感。",
            "ability": "拥有灵敏的嗅觉和听觉，擅长寻找和制作真实食物，尾毛蓬松柔软，带着阳光烘烤过的暖意。",
            "background": "71492d772f5e0834be6ce7aef5b70f45.jpg"
        },
        "乌鸦": {
            "name": "顾淮",
            "identity": "永生之地B栋医生，沈宴的挚友，因牵连入狱，专注研究降低污染值的方法，冷静理智的科研型人才。",
            "appearance": "身材修长挺拔，白大褂勾勒平直肩线与劲瘦腰身，面容冷峻，凤眼凌厉眼尾微挑，肤色冷白，眉骨有一颗浅淡泪痣，气质疏离如冰山。",
            "personality": "理性克制，逻辑缜密，对外人冷漠疏离，对沈宴忠诚；对昼眠从试探到依赖，精神体互动时会因羞涩耳根泛红，本质是'孤独的乌鸦国王'。",
            "ability": "精通医疗与精神检测，污染值曾达98，后因昼眠'深度链接'持续降至安全值，精神体为华贵乌鸦，精神海为孤崖木屋。",
            "background": "68dc3117a8f3f65283551a65302e421f.jpg"
        },
        "狮子": {
            "name": "秦厌",
            "identity": "永生之地A栋老大之一（与温朝惜共同管理），昼眠的舍友，实力强悍的'土著'囚犯，在A栋拥有绝对话语权。",
            "appearance": "蜜色肌肤，肌肉线条漂亮，常穿黑色背心与工装裤，腰绑刀枪，脚踩黑靴；剑眉星目，宽腰窄臀，睡时睫毛投下细影如'收起爪子的狐狸'，眉尾一道浅疤添痞气，笑时像'浸在蜂蜜里的威士忌'，沙哑醇厚。",
            "personality": "表面桀骜暴躁，实则护短心软，对昼眠有'爹咪'式纵容（如训话、担心被拐），烟瘾重却会因昼眠一句话戒烟；看似冷漠，却会在昼眠失踪时暴怒欲拆A栋，本质是'口嫌体正直'的硬汉，对认可的人极度护短。",
            "ability": "A栋顶尖战力，精神体为威严雄狮，擅长近身格斗和武器使用，在A栋拥有绝对话语权。",
            "background": "fe9ed9a8d2d1f61cd998ddab78805efb.jpg"
        },
        "人鱼": {
            "name": "温朝惜",
            "identity": "永生之地A栋老大之一（与秦厌共同管理），昼眠的'饭搭子'，实力强悍的管理者，以温和表象掩盖冷静决断力。",
            "appearance": "肤色冷白，眉眼清淡如宣纸上的水墨，戴金丝眼镜，周身书卷气；身形高挑，穿简约衣物却显清隽，站在血泊中如'雨打湿的白山茶'，自带清冷疏离感。",
            "personality": "表面温润有礼，说话声清透如'风吹竹林'，耐心包容（如陪昼眠吃饭、递糖）；实则冷静理智，管理A栋事务井井有条，与秦厌形成'一文一武'搭档，对昼眠有'爹咪'式关怀（如训话、担心安全）。",
            "ability": "A栋强者之一，擅长以柔克刚（欢迎仪式上与昼眠交手后主动认输），精神力内敛，声音有安抚人心的力量，是A栋秩序的隐形维护者。",
            "background": "686c61493d2304917cb99d74f95071e6.jpg"
        }
    },
    # A级角色 - 贵族
    "A": {
        "兽人": {
            "name": "兽人贵族",
            "identity": "雷霆部落的贵族后裔，拥有古老的狮族血统和强大的战斗天赋。",
            "appearance": "金色鬃毛如同阳光般耀眼，琥珀色的眼眸中闪烁着智慧与力量，身着镶嵌宝石的传统战甲。",
            "personality": "骄傲但不傲慢，重视荣誉与承诺，对族人极度忠诚，在战场上勇猛无畏，在和平时期睿智仁慈。",
            "ability": "狮族特有的雷霆咆哮能震慑敌人，变身成巨狮形态时力量倍增，擅长战略指挥和近身格斗。",
            "background": "1aa1bf749c794e806bdd3d25508547b3.jpg"
        },
        "虫族": {
            "name": "虫族贵族", 
            "identity": "幻影虫巢的高级贵族，掌握着虫族的精神网络和暗杀部队。",
            "appearance": "深紫色甲壳如同水晶般剔透，复眼闪烁着神秘的流光，翅膀薄如蝉翼却坚不可摧。",
            "personality": "优雅而致命，思维缜密如精密仪器，对女皇绝对忠诚，擅长在暗处运筹帷幄。",
            "ability": "精神感应网络能连接整个虫族，幻影分身可迷惑敌人，毒刺攻击一击毙命。",
            "background": "e67189cd7c960bcd85a47cb1e6a62e26.jpg"
        }
    },
    # B级角色 - 平民
    "B": {
        "兽人": {
            "name": "平民",
            "identity": "铁匠世家的传人，在星际港口经营着一家武器铺。",
            "appearance": "结实的肌肉彰显着铁匠的功底，手掌布满老茧，眼神中透着兽人特有的坚韧。",
            "personality": "勤劳朴实，重视信誉，对朋友两肋插刀，有着兽人传统的豪爽与真诚。",
            "ability": "精通各种武器锻造，力量惊人，在恶劣环境中拥有极强的生存能力。",
            "background": "1aa1bf749c794e806bdd3d25508547b3.jpg"
        },
        "虫族": {
            "name": "平民",
            "identity": "工兵虫族的一员，负责建设和维护虫族基地的基础设施。",
            "appearance": "翠绿色的甲壳便于在丛林中伪装，前肢进化成了适合工作的工具形态。",
            "personality": "勤恳敬业，服从命令，有着虫族特有的集体荣誉感，工作一丝不苟。",
            "ability": "快速建造各种设施，甲壳硬化防御，信息素沟通与团队协作。",
            "background": "e67189cd7c960bcd85a47cb1e6a62e26.jpg"
        }
    },
    # C级角色 - 陌生人
    "C": {
        "兽人": {
            "name": "陌生人", 
            "identity": "从远方星系来的兽人商人，带着神秘的货物和故事。",
            "appearance": "穿着适应各种气候的旅行装，背包里装满了各星系的奇珍异宝。",
            "personality": "见多识广但保持低调，善于观察，对陌生文化充满好奇和尊重。",
            "ability": "多语言沟通，星际导航，危险预感和自卫技巧。",
            "background": "1aa1bf749c794e806bdd3d25508547b3.jpg"
        },
        "虫族": {
            "name": "陌生人",
            "identity": "虫族探索舰队成员，负责侦查未知星域和资源点。",
            "appearance": "银白色甲壳反射着星光，翅膀适应长途飞行，复眼能捕捉微弱光线。",
            "personality": "谨慎细心，记录详尽，对未知既警惕又兴奋，忠诚执行探索任务。",
            "ability": "环境适应力强，资源探测，星际定位和生存技能。",
            "background": "1aa1bf749c794e806bdd3d25508547b3.jpg"
        }
    },
    # D级角色 - 被厌恶者
    "D": {
        "兽人": {
            "name": "兽人奴隶",
            "identity": "因挑战部落传统而被驱逐的前武士。",
            "appearance": "身上布满战斗留下的疤痕，眼神中混合着愤怒与悔恨。",
            "personality": "孤僻多疑，不轻易相信他人，内心深处仍保留着兽人的荣誉感。",
            "ability": "潜行与暗杀技巧，在绝境中求生的本能，独自作战的能力。",
            "background": "1aa1bf749c794e806bdd3d25508547b3.jpg"
        },
        "虫族": {
            "name": "虫族奴隶",
            "identity": "提出与传统虫族思维不同理论的学者。",
            "appearance": "甲壳颜色与普通虫族差异明显，复眼呈现出罕见的赤红色。",
            "personality": "独立思考，勇于质疑，因理念不同而感到孤独但坚持己见。",
            "ability": "独特的理论体系，创新能力，说服力和逻辑思维。",
            "background": "1aa1bf749c794e806bdd3d25508547b3.jpg"
        }
    },
    # E级角色 - 被针对者  
    "E": {
        "兽人": {
            "name": "兽人贵族",
            "identity": "以武力挑战现有秩序的流浪武士。",
            "appearance": "战甲上满是战斗痕迹，手持染血的双斧，气势逼人。",
            "personality": "自信到近乎狂妄，追求力量的极致，不承认任何高于自己的权威。",
            "ability": "狂暴战斗状态，双武器精通，战术突破和领导叛乱。",
            "background": "4e8e2b4e138843c689ddc4cf3d507345.jpg"
        },
        "虫族": {
            "name": "虫族贵族",
            "identity": "试图建立新虫巢的分离主义者。",
            "appearance": "甲壳呈现深黑色，外形更加凶猛，散发着危险的气息。",
            "personality": "野心勃勃，不满足于现状，相信自己的力量能够改变虫族命运。",
            "ability": "独立精神网络，特殊进化能力，策略谋划和煽动能力。",
            "background": "f1ec2464-7046-4fea-b124-daaca47e0133.jpg"
        }
    },
    # F级角色 - 皇族威胁
    "F": {
        "兽人": {
            "name": "兽人贵族",
            "identity": "兽人帝国直系贵族，拥有最纯正的远古血统。",
            "appearance": "金色鬃毛中夹杂着银色条纹，皇族战甲镶嵌着传承千年的宝石。",
            "personality": "天生的领导者，威严不容挑衅，智慧与力量并重，肩负整个兽人族的命运。",
            "ability": "皇族血脉的远古力量，兽神祝福，统御万兽的天赋能力。",
            "background": "54eb51160856139cf6d63429fa608457.jpg"
        },
        "虫族": {
            "name": "虫皇",
            "identity": "虫族的至高存在，跨越维度的古老意识。",
            "appearance": "形态不断变化，甲壳如同流动的黑暗，眼中蕴含着整个宇宙的星辰。",
            "personality": "超越凡物的思维，既仁慈又残酷，为了虫族进化可以牺牲一切。",
            "ability": "创造与毁灭的力量，操控时空，心灵感应覆盖整个星系。",
            "background": "e8499f5305a217ff094d74ad5bb47a96.jpg"
        }
    }
}

# 好感等级描述
grade_descriptions = {
    "S": "太棒了！你是他最得力的伙伴和战友！\n精神力等级高达S级，属于名副其实的'皇'族！",
    "A": "太棒了！你是他需要守护的对象！\n精神力等级高达A级，属于名副其实的贵族！",
    "B": "太棒了！你是他普普通通的熟人！\n精神力等级B级，属于平民百姓！",
    "C": "太棒了！你是他平平无奇、不认识的陌生人！\n精神力等级C级，属于平民百姓！",
    "D": "太棒了！你是他厌恶的对象！\n精神力等级B级，属于平民百姓！",
    "E": "太棒了！你是他想除掉的对象！\n精神力等级A级，属于贵族！",
    "F": "太棒了！你是他觉得威胁的存在！\n精神力等级S级，属于名副其实的'皇'族！"
}

class Button:
    def __init__(self, x, y, width, height, text, font=normal_font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.is_hovered = False
        
    def draw(self, surface):
        color = BUTTON_HOVER if self.is_hovered else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect, border_radius=12)
        pygame.draw.rect(surface, TEXT_COLOR, self.rect, 2, border_radius=12)
        
        text_surf = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False



    


def draw_text_wrapped(surface, text, font, color, rect, line_spacing=5):
    """支持中文的文本换行函数，返回实际使用的高度"""
    chars = list(text)
    lines = []
    current_line = []
    
    for char in chars:
        test_line = ''.join(current_line + [char])
        test_surf = font.render(test_line, True, color)
        
        if test_surf.get_width() <= rect.width or char in ['\n', '。', '！', '？']:
            current_line.append(char)
            if char == '\n':
                lines.append(''.join(current_line).rstrip('\n'))
                current_line = []
        else:
            if current_line:
                lines.append(''.join(current_line))
            current_line = [char]
    
    if current_line:
        lines.append(''.join(current_line))
    
    y = rect.top
    for line in lines:
        if y + font.get_height() > rect.bottom:
            # 如果超出区域，添加省略号
            if lines.index(line) > 0:
                last_line = lines[lines.index(line) - 1]
                if len(last_line) > 3:
                    last_line = last_line[:-3] + '...'
                lines[lines.index(line) - 1] = last_line
            break
        text_surf = font.render(line, True, color)
        surface.blit(text_surf, (rect.left, y))
        y += font.get_height() + line_spacing
    
    return min(y - rect.top, rect.height)  # 返回实际使用的高度




def welcome_screen():
    start_button = Button(SCREEN_WIDTH//2 - 100, 500, 200, 60, "开始游戏", header_font)
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(mouse_pos):
                    return "grade_selection"


            if background_image:
                    screen.blit(background_image, (0, 0))
            else:
                    screen.fill(BACKGROUND)
      
       
        current_bg = get_background_for_screen("welcome")
        if current_bg:
                 screen.blit(current_bg, (0, 0))
        else:
                 screen.fill(BACKGROUND)


                

# 绘制
# 向下平移量（根据需要调整这个数值）
        offset_y = 100  # 向下平移50像素
       
        title = title_font.render("欢迎来到星际世界！", True, TITLE_COLOR)
        #title = hint_font.render("欢迎来到星际世界！", True, TITLE_COLOR)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 100 +offset_y ))
        
        descriptions = [
            "玩偶师等您良久！这是一个选择身份界面~~",
            "猜猜昼眠对你的好感等级是多少？",
            "决定你来到他的世界存活率是多少。",
            "亲爱的玩家，想要开启游戏，基本的自我认知可必不可少。"
        ]
        
        for i, desc in enumerate(descriptions):
            text = normal_font.render(desc, True,WHITE )
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, 200 + i * 40+offset_y ))
        
        start_button.check_hover(mouse_pos)
        start_button.draw(screen)
        
        pygame.display.flip()










       

        

def grade_selection_screen():
    grades = ["S", "A", "B", "C", "D", "E", "F"]
    buttons = []
    
    # 创建等级按钮 - 两行布局
    for i, grade in enumerate(grades):
        if i < 4:  # 第一行
            x = 150 + i * 200
            y = 300
        else:  # 第二行
            x = 250 + (i - 4) * 200
            y = 400
        
        buttons.append(Button(x, y, 150, 60, f"{grade}级", header_font))
    
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return "quit", None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.rect.collidepoint(mouse_pos):
                        return "race_selection", grades[i]
            if background_image:
                    screen.blit(background_image, (0, 0))
            else:
                    screen.fill(BACKGROUND)
        
        
        
        title = header_font.render("请选择好感等级", True, TITLE_COLOR)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 100))
        
        desc = normal_font.render("猜猜昼眠对你的好感等级是多少？", True, TEXT_COLOR)
        screen.blit(desc, (SCREEN_WIDTH//2 - desc.get_width()//2, 160))
        
        for button in buttons:
            button.check_hover(mouse_pos)
            button.draw(screen)
        
        pygame.display.flip()

def race_selection_screen(grade):
    # 根据等级获取对应的角色选项
    if grade == "S":
        races = list(characters_data["S"].keys())  # 六个特殊角色
    elif grade in ["A", "E"]:
        races = list(characters_data["A"].keys())  # 贵族角色
    elif grade in ["B", "C", "D"]:
        races = list(characters_data["B"].keys())  # 平民角色
    else:  # F级
        races = list(characters_data["F"].keys())  # 皇族角色
    
    buttons = []
    
    # 创建按钮 - 自适应布局
    num_races = len(races)
    if num_races == 6:  # S级 - 两列三行
        for i, race in enumerate(races):
            col = i % 2
            row = i // 2
            x = SCREEN_WIDTH//2 - 220 + col * 250
            y = 280 + row * 100
            buttons.append(Button(x, y, 200, 60, race, normal_font))
    else:  # 其他等级 - 单列居中
        for i, race in enumerate(races):
            x = SCREEN_WIDTH//2 - 100
            y = 300 + i * 80
            buttons.append(Button(x, y, 200, 60, race, normal_font))
    
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return "quit", None, None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.rect.collidepoint(mouse_pos):
                        return "character_display", grade, races[i]
            if background_image:
                    screen.blit(background_image, (0, 0))
            else:
                    screen.fill(BACKGROUND)
        
       
        
        title = header_font.render(f"好感等级: {grade}级", True, TITLE_COLOR)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 80))
        
        # 等级描述
        desc_text = grade_descriptions[grade]
        desc_lines = desc_text.split('\n')
        for i, line in enumerate(desc_lines):
            text = small_font.render(line, True, TEXT_COLOR)
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, 130 + i * 30))
        
        prompt = normal_font.render("请选择种族", True, HIGHLIGHT_COLOR)
        screen.blit(prompt, (SCREEN_WIDTH//2 - prompt.get_width()//2, 200))
        
        for button in buttons:
            button.check_hover(mouse_pos)
            button.draw(screen)
        
        pygame.display.flip()

def character_display_screen(grade, race):
    back_button = Button(50, 50, 100, 40, "返回", small_font)
    finish_button = Button(SCREEN_WIDTH-150, SCREEN_HEIGHT-80, 100, 40, "完成", small_font)
    
    # 根据等级获取对应的角色数据
    if grade == "S":
        character = characters_data["S"][race]
    elif grade in ["A", "E"]:
        character = characters_data["A"][race]
    elif grade in ["B", "C", "D"]:
        character = characters_data["B"][race]
    else:  # F级
        character = characters_data["F"][race]
    
    # 创建滚动区域
    scroll_y = 0
    max_scroll = 0
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return "quit"
            
            # 鼠标滚轮事件
            if event.type == pygame.MOUSEWHEEL:
                scroll_y -= event.y * 30  # 滚动速度
                scroll_y = max(-max_scroll, min(0, scroll_y))  # 限制滚动范围
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(mouse_pos):
                    return "race_selection", grade
                elif finish_button.rect.collidepoint(mouse_pos):
                    return "completion", grade, race
            
        
        current_bg = get_background_for_screen("character_display", grade, race)
        if current_bg:
            screen.blit(current_bg, (0, 0))
        else:
            screen.fill(BACKGROUND)
        # 绘制背景
   
        
        # 创建表面用于滚动内容（设置透明背景）
        content_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT * 2), pygame.SRCALPHA)
        content_surface.fill((0, 0, 0, 0))  # 完全透明







        
        
   
        
        # 角色标题
        title = title_font.render(f"角色生成成功！", True, TITLE_COLOR)
        content_surface.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 20))
        
        # 角色名称和等级
        name_text = header_font.render(f"{character['name']} ({race}) - {grade}级", True, HIGHLIGHT_COLOR)
        content_surface.blit(name_text, (SCREEN_WIDTH//2 - name_text.get_width()//2, 90))
        
        # 角色详细信息
        y_pos = 160
        sections = [
            ("身份", character["identity"]),
            ("外貌", character["appearance"]),
            ("性格", character["personality"]),
            ("能力", character["ability"])
        ]
        
        for section, content in sections:
            # 分段标题
            section_title = header_font.render(f"【{section}】", True, HIGHLIGHT_COLOR)
            content_surface.blit(section_title, (80, y_pos))
            y_pos += 40
            
            # 分段内容 - 使用更大的显示区域
            content_rect = pygame.Rect(100, y_pos, SCREEN_WIDTH-200, 400)
            actual_height = draw_text_wrapped(content_surface, content, small_font, TEXT_COLOR, content_rect, 8)
            y_pos += actual_height + 40
        
        # 计算最大滚动距离
        max_scroll = max(0, y_pos - SCREEN_HEIGHT + 200)
        
        # 绘制滚动内容
        screen.blit(content_surface, (0, scroll_y))
        
        # 绘制固定位置的按钮（不随内容滚动）
        back_button.check_hover(mouse_pos)
        back_button.draw(screen)
        finish_button.check_hover(mouse_pos)
        finish_button.draw(screen)
        
        # 显示滚动提示（如果需要滚动）
        if max_scroll > 0:
            scroll_hint = small_font.render("使用鼠标滚轮滚动查看完整内容", True, (200, 200, 200))
            screen.blit(scroll_hint, (SCREEN_WIDTH//2 - scroll_hint.get_width()//2, SCREEN_HEIGHT - 40))
        
        pygame.display.flip()

#第一个版本保留了背景
#第二个版本是黑色背景
#第三个版本最后开始闪了两下
#第四个版本开始测试！测试失败！
#第五个版本开始测试！测试失败！
#第六版成功！
def enhanced_countdown_effect():
    """最稳定版本 - 使用delay"""
    print("🚀 开始稳定版倒计时...")
    
    countdown_font = pygame.font.SysFont("simhei", 200, bold=True)
    colors = [(255, 50, 50), (255, 165, 0), (50, 255, 50)]
    
    for number in [3, 2, 1]:
        print(f"显示数字: {number}")
        
        # 绘制数字
        screen.fill((0, 0, 0))
        number_text = countdown_font.render(str(number), True, colors[number-1])
        screen.blit(number_text, (SCREEN_WIDTH//2 - number_text.get_width()//2, 
                                SCREEN_HEIGHT//2 - number_text.get_height()//2))
        pygame.display.flip()
        
        # 使用delay但期间处理事件
        delay_time = 1000  # 1秒
        chunk = 100  # 每100ms检查一次事件
        chunks = delay_time // chunk
        
        for _ in range(chunks):
            pygame.time.delay(chunk)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_SPACE, pygame.K_ESCAPE, pygame.K_s]:
                        return True
    
    # 显示"开始！"
    print("显示'开始！'")
    screen.fill((0, 0, 0))
    start_text = countdown_font.render("开始！", True, (0, 255, 255))
    screen.blit(start_text, (SCREEN_WIDTH//2 - start_text.get_width()//2, 
                           SCREEN_HEIGHT//2 - start_text.get_height()//2))
    pygame.display.flip()
    
    # 等待0.5秒
    delay_time = 500
    chunk = 100
    chunks = delay_time // chunk
    
    for _ in range(chunks):
        pygame.time.delay(chunk)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_SPACE, pygame.K_ESCAPE, pygame.K_s]:
                    return True
    
    print("✅ 倒计时完成！")
    return True

def story_scene(grade, race):
    """剧情场景 - 确保能正常运行"""
    print(f"🎭 进入剧情场景: grade={grade}, race={race}")
    
    # 简单的返回按钮
    back_button = Button(50, 50, 100, 40, "返回", small_font)
    
    # 获取角色信息
    try:
        if grade == "S":
            character = characters_data["S"][race]
        elif grade in ["A", "E"]:
            character = characters_data["A"][race]
        elif grade in ["B", "C", "D"]:
            character = characters_data["B"][race]
        else:
            character = characters_data["F"][race]
    except:
        character = {"name": "未知角色"}
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button.rect.collidepoint(mouse_pos):
                    print("↩️ 返回完成界面")
                    return "completion", grade, race
        
        # 简单背景
        screen.fill(BACKGROUND)
        
        # 显示剧情文本
        title = title_font.render("剧情场景", True, TITLE_COLOR)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 100))
        
        story_text = normal_font.render(f"欢迎{character['name']}!您的星际冒险即将开始！", True, WHITE)
        screen.blit(story_text, (SCREEN_WIDTH//2 - story_text.get_width()//2, 200))
        
        hint_text = small_font.render("剧情内容开发中...", True, SILVER)
        screen.blit(hint_text, (SCREEN_WIDTH//2 - hint_text.get_width()//2, 300))
        
        # 绘制返回按钮
        back_button.check_hover(mouse_pos)
        back_button.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    return "completion", grade, race



def completion_screen(grade, race):
    print(f"🎮 进入完成界面: grade={grade}, race={race}")
    """完成界面 - 显示最终结果"""
    # 在函数内部定义字体
    font = pygame.font.SysFont("simsun", 28)
    
    # 获取角色信息
    try:
        if grade == "S":
            character_info = characters_data["S"][race]
        elif grade in ["A", "E"]:
            character_info = characters_data["A"][race]
        elif grade in ["B", "C", "D"]:
            character_info = characters_data["B"][race]
        else:  # F级
            character_info = characters_data["F"][race]
    except KeyError:
        character_info = {
            "name": "未知角色", 
            "identity": "未知身份",
            "ability": "未知能力",
            "affection": "未知"
        }
    
    # 创建按钮
    restart_button = Button(SCREEN_WIDTH//2 - 100, 550, 200, 60, "重新开始", button_font)
    quit_button = Button(SCREEN_WIDTH//2 - 100, 630, 200, 60, "退出游戏", button_font)
    start_story_button = Button(SCREEN_WIDTH//2 - 100, 450, 200, 60, "开始剧情", button_font)

    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return "quit"
            #增加调试部分的版本
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_story_button.rect.collidepoint(mouse_pos):
                    # 先显示倒计时特效，然后进入剧情
                    if enhanced_countdown_effect():
                        return "story_scene", grade, race

                if restart_button.rect.collidepoint(mouse_pos):
                    return "welcome"
                if quit_button.rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                    return "quit"
               
            #增加停在这里
                



                    
        
        # 绘制背景
        try:
            current_bg = get_background_for_screen("completion", grade, race)
            if current_bg:
                screen.blit(current_bg, (0, 0))
            else:
                screen.fill(BACKGROUND)
        except:
             screen.fill(BACKGROUND)
        
        # 绘制标题
        title_text = title_font.render("恭喜！星际玩偶师资格认证完成！", True, GOLD)
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 80))



         # 绘制角色信息卡片 - 紧凑设计
        card_rect = pygame.Rect(SCREEN_WIDTH//2 - 200, 180, 400, 200)
        pygame.draw.rect(screen, (40, 40, 70, 180), card_rect, border_radius=15)
        pygame.draw.rect(screen, GOLD, card_rect, 3, border_radius=15)
        
        # 显示核心信息（4行）
        info_texts = [
            (f"{grade}级玩偶师", GOLD, 200),
            (f"专属身份：{race}", LIGHT_BLUE, 240),
            (f"角色：{character_info['name']}", WHITE, 280),
            (f"初始好感度：{character_info.get('affection', '未知')}", (255, 182, 193), 320)
        ]        
        for text, color, y_pos in info_texts:
            text_surface = header_font.render(text, True, color) if y_pos <= 280 else font.render(text, True, color)
            screen.blit(text_surface, (SCREEN_WIDTH//2 - text_surface.get_width()//2, y_pos))
        # 绘制按钮
        restart_button.draw(screen)
        quit_button.draw(screen)
        start_story_button.check_hover(mouse_pos)
        start_story_button.draw(screen)
        restart_button.check_hover(mouse_pos)
        quit_button.check_hover(mouse_pos)



        
        # 底部提示
        hint_text = small_font.render("准备好开始你的星际冒险了吗？", True, SILVER)
        screen.blit(hint_text, (SCREEN_WIDTH//2 - hint_text.get_width()//2, 720))
        
        pygame.display.flip()
        clock.tick(60)
        #增加显示跳过提示
        skip_text = small_font.render("按 S 键跳过倒计时", True, (200, 200, 200))
        screen.blit(skip_text, (SCREEN_WIDTH - skip_text.get_width() - 20, 20))
        
        pygame.display.flip()
        clock.tick(60)
    
    return "welcome"



    if background_image:
                    screen.blit(background_image, (0, 0))
    else:
                    screen.fill(BACKGROUND)

            
        
    screen.fill(BACKGROUND)
        
    title = title_font.render("🎊 CONGRATULATIONS! 🎊", True, TITLE_COLOR)
    screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 120))
        
    msg1 = header_font.render("属性档案建立完成！", True, HIGHLIGHT_COLOR)
    screen.blit(msg1, (SCREEN_WIDTH//2 - msg1.get_width()//2, 200))
        
    msg2 = header_font.render("请享受独属于您的星际征程！", True, TEXT_COLOR)
    screen.blit(msg2, (SCREEN_WIDTH//2 - msg2.get_width()//2, 250))
        
    summary = normal_font.render(f"最终角色: {character['name']} ({race})", True, TEXT_COLOR)
    screen.blit(summary, (SCREEN_WIDTH//2 - summary.get_width()//2, 320))
        
    grade_text = normal_font.render(f"好感等级: {grade}级", True, HIGHLIGHT_COLOR)
    screen.blit(grade_text, (SCREEN_WIDTH//2 - grade_text.get_width()//2, 360))
        
    restart_button.check_hover(mouse_pos)
    restart_button.draw(screen)
    
    pygame.display.flip()


# ========== 添加 Loading 动画函数 ==========
def show_loading_screen():
    """显示加载动画"""
    print("🚀 开始加载游戏资源...")
    
    # 创建加载界面背景
    loading_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    loading_bg.fill((10, 15, 40))  # 深蓝色星空背景
    
    # 添加星星背景
    for i in range(50):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        size = random.randint(1, 2)
        brightness = random.randint(100, 200)
        pygame.draw.circle(loading_bg, (brightness, brightness, brightness), (x, y), size)
    
    # 加载文字
    loading_font = pygame.font.SysFont("simhei", 36)
    title_font = pygame.font.SysFont("simhei", 48, bold=True)
    
    # 旋转的加载图标点
    dots = ["●", "●", "●"]
    dot_colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]
    dot_angle = 0
    
    # 进度条
    progress = 0
    progress_width = 600
    progress_height = 20
    progress_rect = pygame.Rect(SCREEN_WIDTH//2 - progress_width//2, 500, progress_width, progress_height)
    
    # 模拟加载过程
    start_time = pygame.time.get_ticks()
    loading = True
    
    while loading:
        current_time = pygame.time.get_ticks()
        elapsed = current_time - start_time
        
        # 更新进度（3秒完成加载）
        progress = min(elapsed / 3000, 1.0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return False
        
        # 绘制背景
        screen.blit(loading_bg, (0, 0))
        
        # 绘制标题
        title_text = title_font.render("星际玩偶师", True, GOLD)
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 150))
        
        # 绘制副标题
        subtitle = loading_font.render("正在初始化星河系统...", True, LIGHT_BLUE)
        screen.blit(subtitle, (SCREEN_WIDTH//2 - subtitle.get_width()//2, 220))
        
        # 绘制旋转的加载图标
        dot_angle += 0.2
        center_x, center_y = SCREEN_WIDTH//2, 350
        radius = 30
        
        for i, dot in enumerate(dots):
            angle = dot_angle + i * (2 * 3.14159 / 3)  # 三个点均匀分布
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            dot_text = loading_font.render(dot, True, dot_colors[i])
            screen.blit(dot_text, (x - dot_text.get_width()//2, y - dot_text.get_height()//2))
        
        # 绘制进度条背景
        pygame.draw.rect(screen, (50, 50, 80), progress_rect, border_radius=10)
        pygame.draw.rect(screen, (80, 80, 120), progress_rect, 2, border_radius=10)
        
        # 绘制进度条填充 - 完全修复颜色问题
        if progress > 0:
            fill_width = int(progress_width * progress)
            fill_rect = pygame.Rect(progress_rect.left, progress_rect.top, fill_width, progress_height)
            
            # 直接使用明确的颜色值，不使用变量
            if progress < 0.5:
                bar_color = (100, 100, 255)  # 蓝色
            elif progress < 0.8:
                bar_color = (100, 200, 255)  # 蓝绿色
            else:
                bar_color = (100, 255, 200)  # 绿色
            
            pygame.draw.rect(screen, bar_color, fill_rect, border_radius=10)
        
        # 绘制进度文字
        percent = int(progress * 100)
        percent_text = loading_font.render(f"{percent}%", True, WHITE)
        screen.blit(percent_text, (SCREEN_WIDTH//2 - percent_text.get_width()//2, 530))
        
        # 绘制加载提示
        tips = [
            "正在连接星河网络...",
            "初始化玩偶师系统...",
            "加载角色数据库...",
            "准备星际传送门...",
            "校准精神力传感器..."
        ]
        
        tip_index = min(int(progress * len(tips)), len(tips) - 1)
        tip_text = small_font.render(tips[tip_index], True, SILVER)
        screen.blit(tip_text, (SCREEN_WIDTH//2 - tip_text.get_width()//2, 580))
        
        # 绘制版权信息
        copyright_text = small_font.render("© 李璐 荣誉出品", True, (150, 150, 180))
        screen.blit(copyright_text, (SCREEN_WIDTH//2 - copyright_text.get_width()//2, 700))
        
        pygame.display.flip()
        clock.tick(60)
        
        # 检查是否完成加载
        if progress >= 1.0:
            loading = False
            # 添加一个完成的闪烁效果
            for i in range(3):
                screen.blit(loading_bg, (0, 0))
                complete_text = title_font.render("加载完成！", True, (0, 255, 0))  # 直接使用绿色
                screen.blit(complete_text, (SCREEN_WIDTH//2 - complete_text.get_width()//2, 350))
                pygame.display.flip()
                pygame.time.delay(300)
            
            pygame.time.delay(500)  # 额外延迟让玩家看到完成状态
    
    print("✅ 游戏资源加载完成！")
    return True
# ========== 主函数 ==========

def main():
    # 显示加载动画
    if not show_loading_screen():
        return  # 如果加载过程中退出，直接返回
    
    current_screen = "welcome"
    game_data = {}
    
    while True:
        if current_screen == "welcome":
            current_screen = welcome_screen()
        
        elif current_screen == "grade_selection":
            result = grade_selection_screen()
            if result[0] == "quit":
                break
            current_screen, grade = result
            game_data["grade"] = grade
        
        elif current_screen == "race_selection":
            result = race_selection_screen(game_data["grade"])
            if result[0] == "quit":
                break
            current_screen, grade, race = result
            game_data["race"] = race
        
        elif current_screen == "character_display":
            result = character_display_screen(game_data["grade"], game_data["race"])
            if result[0] == "quit":
                break
            elif result[0] == "race_selection":
                current_screen, grade = result
                game_data["grade"] = grade
            else:
                current_screen, grade, race = result
                game_data["grade"] = grade
                game_data["race"] = race
        
        elif current_screen == "completion":
            result = completion_screen(game_data["grade"], game_data["race"])
            if result == "quit":
                break
            elif isinstance(result, tuple) and len(result) == 3:  # 处理 (story_scene, grade, race)
                current_screen, grade, race = result
                game_data["grade"] = grade
                game_data["race"] = race
            else:
                current_screen = result
        
        # 新增剧情场景处理
        elif current_screen == "story_scene":
            result = story_scene(game_data["grade"], game_data["race"])
            if result == "quit":
                break
            elif isinstance(result, tuple) and len(result) == 3:
                current_screen, grade, race = result
                game_data["grade"] = grade
                game_data["race"] = race
            else:
                current_screen = result
        
        elif current_screen == "quit":
            break

if __name__ == "__main__":
    main()
    pygame.quit()
#以下正在测试中，尚不能使用。
  

# 在角色数据后添加剧情数据
story_data = {
    "chapter_1": {
        "title": "初入永生之地",
        "scenes": {
            "scene_1_1": {
                "background": "prison_entrance.jpg",
                "dialogue": [
                    {
                        "character": "system",
                        "name": "系统",
                        "text": "你醒来发现自己身处一个陌生的牢房...",
                        "expression": "neutral"
                    },
                    {
                        "character": "player", 
                        "name": "你",
                        "text": "这是哪里？我的头好痛...",
                        "expression": "confused"
                    },
                    {
                        "character": "黑猫",
                        "name": "宋惊澜",
                        "text": "新来的？看起来不太适应这里的环境。",
                        "expression": "cold"
                    }
                ],
                "choices": [
                    {
                        "text": "礼貌询问", 
                        "next_scene": "scene_1_2",
                        "effect": {"affection": 5}
                    },
                    {
                        "text": "警惕质问", 
                        "next_scene": "scene_1_3", 
                        "effect": {"affection": -3}
                    }
                ]
            },
            "scene_1_2": {
                "background": "prison_corridor.jpg",
                "dialogue": [
                    # 更多对话...
                ],
                "choices": [
                    # 更多选择...
                ]
            }
        }
    },
    "chapter_2": {
        # 第二章剧情...
    }
}

class StoryManager:
    def __init__(self):
        self.current_chapter = None
        self.current_scene = None
        self.character_affection = {}  # 角色好感度
        self.story_progress = {}  # 剧情进度
        self.player_choices = []  # 玩家选择记录
        
    def start_chapter(self, chapter_id, grade, race):
        """开始新章节"""
        self.current_chapter = chapter_id
        self.current_scene = f"{chapter_id}_1"  # 章节第一幕
        self.player_grade = grade
        self.player_race = race
        
    def get_current_scene_data(self):
        """获取当前场景数据"""
        if self.current_chapter and self.current_scene:
            return story_data[self.current_chapter]["scenes"][self.current_scene]
        return None
        
    def make_choice(self, choice_index):
        """处理玩家选择"""
        scene_data = self.get_current_scene_data()
        if scene_data and choice_index < len(scene_data["choices"]):
            choice = scene_data["choices"][choice_index]
            
            # 记录选择
            self.player_choices.append({
                "scene": self.current_scene,
                "choice": choice["text"],
                "timestamp": pygame.time.get_ticks()
            })
            
            # 应用效果
            if "effect" in choice:
                self.apply_effect(choice["effect"])
            
            # 跳转到下一场景
            self.current_scene = choice["next_scene"]
            return True
        return False
    
    def apply_effect(self, effect):
        """应用选择效果"""
        if "affection" in effect:
            # 更新好感度逻辑
            pass


def story_scene(grade, race, chapter_id="chapter_1"):
    """增强版剧情场景"""
    # 初始化剧情管理器
    story_manager = StoryManager()
    story_manager.start_chapter(chapter_id, grade, race)
    
    # 创建UI元素
    back_button = Button(50, 50, 100, 40, "返回", small_font)
    next_button = Button(SCREEN_WIDTH-150, SCREEN_HEIGHT-100, 100, 40, "继续", small_font)
    
    # 对话框
    dialog_rect = pygame.Rect(100, SCREEN_HEIGHT - 250, SCREEN_WIDTH - 200, 180)
    
    # 选择按钮
    choice_buttons = []
    
    # 文本显示控制
    current_dialog_index = 0
    typing_text = ""
    typing_progress = 0
    typing_speed = 2  # 字符/帧
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        current_scene_data = story_manager.get_current_scene_data()
        
        if not current_scene_data:
            # 剧情结束
            return "completion", grade, race
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 检查选择按钮点击
                for i, button in enumerate(choice_buttons):
                    if button.rect.collidepoint(mouse_pos):
                        story_manager.make_choice(i)
                        choice_buttons = []  # 清空选择
                        current_dialog_index = 0
                        typing_progress = 0
                        break
                
                # 继续按钮
                if next_button.rect.collidepoint(mouse_pos):
                    if current_dialog_index < len(current_scene_data["dialogue"]) - 1:
                        current_dialog_index += 1
                        typing_progress = 0
                    else:
                        # 显示选择或进入下一场景
                        pass
                
                # 返回按钮
                if back_button.rect.collidepoint(mouse_pos):
                    return "completion", grade, race
        
        # 绘制场景
        draw_story_scene(story_manager, current_scene_data, current_dialog_index, 
                        typing_progress, dialog_rect, choice_buttons)
        
        # 更新打字效果
        if typing_progress < len(current_scene_data["dialogue"][current_dialog_index]["text"]):
            typing_progress += typing_speed
        
        pygame.display.flip()
        clock.tick(60)
    
    return "completion", grade, race

def draw_story_scene(story_manager, scene_data, dialog_index, typing_progress, dialog_rect, choice_buttons):
    """绘制剧情场景"""
    # 绘制背景
    bg_image = load_background_image(scene_data["background"])
    if bg_image:
        screen.blit(bg_image, (0, 0))
    else:
        screen.fill(BACKGROUND)
    
    # 绘制角色立绘（如果有）
    if dialog_index < len(scene_data["dialogue"]):
        current_dialog = scene_data["dialogue"][dialog_index]
        if current_dialog["character"] != "system" and current_dialog["character"] != "player":
            draw_character_sprite(current_dialog["character"], current_dialog["expression"])
    
    # 绘制对话框
    pygame.draw.rect(screen, (0, 0, 0, 200), dialog_rect, border_radius=15)
    pygame.draw.rect(screen, SILVER, dialog_rect, 2, border_radius=15)
    
    # 绘制对话
    if dialog_index < len(scene_data["dialogue"]):
        current_dialog = scene_data["dialogue"][dialog_index]
        
        # 角色名字
        name_text = character_name_font.render(current_dialog["name"], True, GOLD)
        screen.blit(name_text, (dialog_rect.left + 20, dialog_rect.top + 15))
        
        # 对话内容（打字机效果）
        display_text = current_dialog["text"][:int(typing_progress)]
        text_rect = pygame.Rect(dialog_rect.left + 20, dialog_rect.top + 60, 
                              dialog_rect.width - 40, dialog_rect.height - 80)
        draw_text_wrapped(screen, display_text, normal_font, WHITE, text_rect)
    
    # 绘制选择按钮（当对话结束时）
    if dialog_index == len(scene_data["dialogue"]) - 1 and typing_progress >= len(scene_data["dialogue"][dialog_index]["text"]):
        if not choice_buttons and "choices" in scene_data:
            choice_buttons = create_choice_buttons(scene_data["choices"], dialog_rect)
        
        for button in choice_buttons:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)
    
    # 绘制继续按钮（当有更多对话时）
    if dialog_index < len(scene_data["dialogue"]) - 1 and typing_progress >= len(scene_data["dialogue"][dialog_index]["text"]):
        next_button = Button(SCREEN_WIDTH-150, SCREEN_HEIGHT-100, 100, 40, "继续", small_font)
        next_button.check_hover(pygame.mouse.get_pos())
        next_button.draw(screen)

def create_choice_buttons(choices, dialog_rect):
    """创建选择按钮"""
    buttons = []
    button_height = 50
    spacing = 10
    total_height = len(choices) * button_height + (len(choices) - 1) * spacing
    start_y = dialog_rect.top - total_height - 20
    
    for i, choice in enumerate(choices):
        button_rect = pygame.Rect(
            dialog_rect.left + 50,
            start_y + i * (button_height + spacing),
            dialog_rect.width - 100,
            button_height
        )
        buttons.append(ChoiceButton(button_rect, choice["text"]))
    
    return buttons

class ChoiceButton:
    """选择按钮类"""
    def __init__(self, rect, text):
        self.rect = rect
        self.text = text
        self.is_hovered = False
        
    def draw(self, surface):
        color = BUTTON_HOVER if self.is_hovered else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, TEXT_COLOR, self.rect, 2, border_radius=8)
        
        text_surf = small_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered

    
class SaveSystem:
    def __init__(self):
        self.save_slots = 3
        
    def save_game(self, slot, story_manager, affection_system):
        """保存游戏"""
        save_data = {
            "timestamp": pygame.time.get_ticks(),
            "story_progress": story_manager.story_progress,
            "character_affection": affection_system.affection_levels,
            "player_choices": story_manager.player_choices,
            "current_scene": story_manager.current_scene
        }
        
        # 实际实现中这里会保存到文件
        print(f"游戏已保存到槽位 {slot}")
        
    def load_game(self, slot):
        """加载游戏"""
        # 从文件加载数据
        print(f"从槽位 {slot} 加载游戏")
        return None  # 返回加载的数据

def main():
    # 显示加载动画
    if not show_loading_screen():
        return
    
    current_screen = "welcome"
    game_data = {}
    story_manager = StoryManager()
    affection_system = AffectionSystem()
    
    while True:
        if current_screen == "welcome":
            current_screen = welcome_screen()
        
        elif current_screen == "grade_selection":
            result = grade_selection_screen()
            if result[0] == "quit":
                break
            current_screen, grade = result
            game_data["grade"] = grade
        
        elif current_screen == "race_selection":
            result = race_selection_screen(game_data["grade"])
            if result[0] == "quit":
                break
            current_screen, grade, race = result
            game_data["race"] = race
        
        elif current_screen == "character_display":
            result = character_display_screen(game_data["grade"], game_data["race"])
            if result[0] == "quit":
                break
            elif result[0] == "race_selection":
                current_screen, grade = result
                game_data["grade"] = grade
            else:
                current_screen, grade, race = result
                game_data["grade"] = grade
                game_data["race"] = race
        
        elif current_screen == "completion":
            result = completion_screen(game_data["grade"], game_data["race"])
            if result == "quit":
                break
            elif isinstance(result, tuple) and result[0] == "story_scene":
                current_screen, grade, race = result
                game_data["grade"] = grade
                game_data["race"] = race
        
        # 增强版剧情场景
        elif current_screen == "story_scene":
            result = story_scene(game_data["grade"], game_data["race"])
            if result == "quit":
                break
            elif isinstance(result, tuple) and len(result) == 3:
                current_screen, grade, race = result
                game_data["grade"] = grade
                game_data["race"] = race
            else:
                current_screen = result
        
        elif current_screen == "quit":
            break

    

# 在完成界面后添加简单互动
def simple_interaction(grade, race):
    """添加简单的问答互动"""
    questions = [
        {
            "question": "遇到危险的星际生物，你会？",
            "choices": ["勇敢战斗", "巧妙躲避", "尝试沟通"],
            "effects": {"勇气": 5, "智慧": 3, "魅力": 4}
        }
    ]
    # 让玩家做出选择，影响角色关系





