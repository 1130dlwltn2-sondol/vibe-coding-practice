#!/usr/bin/env python3
"""바이브 코딩 실전 책용 이미지 생성 스크립트 (PIL 기반)."""
import os
import math
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")

BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

BG = (13, 19, 38)
PANEL = (24, 33, 62)
CORAL = (224, 120, 86)
TEAL = (78, 205, 196)
BLUE = (96, 150, 255)
WHITE = (245, 247, 250)
MUTED = (154, 167, 199)
LINE = (70, 88, 140)
LIGHT_BG = (250, 251, 253)
INK = (30, 41, 59)
SUB = (100, 116, 139)
CARD_LINE = (203, 213, 225)
WARN = (245, 158, 11)
RED = (220, 90, 90)
PURPLE = (139, 92, 246)


def font(path, size):
    return ImageFont.truetype(path, size, index=1)


def text_center(d, cx, y, s, f, fill):
    bb = d.textbbox((0, 0), s, font=f)
    w = bb[2] - bb[0]
    d.text((cx - w / 2 - bb[0], y), s, font=f, fill=fill)


def rrect(d, box, radius, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(d, x1, y1, x2, y2, fill=CORAL, width=4):
    d.line([x1, y1, x2, y2], fill=fill, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    sz = 14
    for da in (2.6, -2.6):
        d.line([x2, y2, x2 + sz * math.cos(ang + da), y2 + sz * math.sin(ang + da)],
               fill=fill, width=width)


# ---------------------------------------------------------------- 표지 1000x1300
def make_cover():
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(13 + (30 - 13) * t)
        g = int(19 + (44 - 19) * t)
        b = int(38 + (82 - 38) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    d.ellipse([-180, -180, 320, 320], outline=(224, 120, 86, 90), width=3)
    d.ellipse([-120, -120, 260, 260], outline=(78, 205, 196, 70), width=2)
    d.ellipse([760, 980, 1180, 1400], outline=(96, 150, 255, 80), width=3)
    d.ellipse([820, 1040, 1120, 1340], outline=(224, 120, 86, 60), width=2)
    for i in range(6):
        x = 700 + i * 45
        d.line([(x, 0), (x + 220, 420)], fill=(255, 255, 255, 14), width=2)
    # 채팅 말풍선 장식
    rrect(d, [90, 200, 320, 300], 18, PANEL, outline=LINE, width=2)
    d.polygon([(150, 300), (190, 300), (150, 330)], fill=PANEL, outline=LINE)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)
    d.text((120, 230), "...", font=fb(40), fill=CORAL)

    text_center(d, W / 2, 66, "W I K I D O C S   T E C H   B O O K", fr(26), CORAL)
    d.line([(120, 128), (880, 128)], fill=LINE, width=2)

    text_center(d, W / 2, 210, "바이브 코딩", fb(92), WHITE)
    text_center(d, W / 2, 330, "실전", fb(92), CORAL)

    text_center(d, W / 2, 500, "코딩을 모르는 사람을 위한", fb(42), WHITE)
    text_center(d, W / 2, 562, "기획·프롬프트·검증 프로젝트형 실전서", fb(42), WHITE)

    rrect(d, [160, 680, 840, 748], 34, PANEL, outline=LINE, width=2)
    text_center(d, W / 2, 696, "기획자·마케터·소상공인·1인 사업자를 위한 책", fb(30), WHITE)

    topics = [
        "바이브 코딩의 원리와 솔직한 한계",
        "AI가 이해하는 명세서 쓰기",
        "작은 단위 프롬프트와 디버깅 대화법",
        "프로젝트 3종: 랜딩·자동화·체험판 검증",
        "AI 챗봇 상담원 만들기",
    ]
    y = 800
    text_center(d, W / 2, y, "이 책에서 다루는 내용", fr(26), MUTED)
    y += 44
    for i, t in enumerate(topics):
        rrect(d, [170, y, 830, y + 46], 23, (20, 28, 54), outline=(60, 76, 120), width=1)
        d.ellipse([194, y + 11, 228, y + 45], fill=CORAL)
        fnum = fb(26)
        num = str(i + 1)
        bb = d.textbbox((0, 0), num, font=fnum)
        d.text((211 - (bb[2] - bb[0]) / 2 - bb[0], y + 13), num, font=fnum, fill=(255, 255, 255))
        d.text((244, y + 15), t, font=fr(24), fill=WHITE)
        y += 56

    d.line([(120, 1130), (880, 1130)], fill=LINE, width=2)
    text_center(d, W / 2, 1158, "저자  순돌", fr(30), MUTED)
    text_center(d, W / 2, 1202, "기준일  2026-10-14", fr(26), MUTED)

    img.save(os.path.join(ASSETS, "cover.png"))
    print("cover.png saved")


# ------------------------------------------- fig-vs-dev: 기존 개발 vs 바이브 코딩
def make_vs_dev():
    W, H = 1500, 760
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "기존 개발 vs 바이브 코딩", fb(40), INK)
    text_center(d, W / 2, 78, "같은 목표, 다른 흐름",
                fr(26), SUB)

    # 좌: 기존 개발
    rrect(d, [40, 150, 710, 640], 20, (255, 255, 255), outline=CARD_LINE, width=2)
    text_center(d, 375, 172, "기존 개발", fb(32), INK)
    steps_old = ["기획서", "설계", "코딩", "테스트", "배포"]
    x = 90
    for i, s in enumerate(steps_old):
        rrect(d, [x, 260, x + 96, 360], 14, (238, 242, 247), outline=BLUE, width=2)
        text_center(d, x + 48, 292, s, fb(22), INK)
        if i < 4:
            arrow(d, x + 100, 310, x + 116, 310, fill=(148, 163, 184), width=4)
        x += 112
    text_center(d, 375, 420, "사람이 코드를 직접 쓴다", fr(24), SUB)
    text_center(d, 375, 460, "정확하지만 느리고, 코드 지식이 필요", fr(24), SUB)
    rrect(d, [90, 520, 620, 590], 12, (239, 246, 255))
    text_center(d, 375, 542, "검증: 코드 리뷰와 테스트", fr(22), SUB)

    # 우: 바이브 코딩
    rrect(d, [790, 150, 1460, 640], 20, (255, 255, 255), outline=CORAL, width=3)
    text_center(d, 1125, 172, "바이브 코딩", fb(32), INK)
    steps_new = ["말로 설명", "AI 생성", "실행 확인", "고치기", "배포"]
    x = 840
    for i, s in enumerate(steps_new):
        rrect(d, [x, 260, x + 96, 360], 14, (255, 243, 235), outline=CORAL, width=2)
        text_center(d, x + 48, 292, s, fb(22), INK)
        if i < 4:
            arrow(d, x + 100, 310, x + 116, 310, fill=(148, 163, 184), width=4)
        x += 112
    arrow(d, 1310, 360, 860, 360, fill=TEAL, width=3)
    text_center(d, 1125, 400, "안 되면 설명을 바꿔 다시 (반복)", fr(22), TEAL)
    text_center(d, 1125, 460, "사람이 기획하고 판단하고 검증한다", fr(24), SUB)
    text_center(d, 1125, 500, "빠르지만, 눈으로 확인해야 한다", fr(24), SUB)
    rrect(d, [840, 540, 1370, 590], 12, (255, 245, 238))
    text_center(d, 1125, 542, "검증: 직접 실행해 보고 사람이 확인", fr(22), SUB)

    img.save(os.path.join(ASSETS, "fig-vs-dev.png"))
    print("fig-vs-dev.png saved")


# ------------------------------------------------- fig-failure-1: 환각 코드
def make_failure_1():
    W, H = 1400, 700
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "실패 패턴 1: 환각 코드", fb(40), INK)
    text_center(d, W / 2, 78, "동작하는 것처럼 보이지만, 로직이 틀렸다",
                fr(26), SUB)

    cards = [
        ("원인", "AI가 문맥을 추측해서\n코드를 채운다", CORAL),
        ("증상", "화면은 뜨지만\n계산·날짜가 틀리다", WARN),
        ("예시", "할인율 10%를\n10.0%로 계산", RED),
    ]
    x0, bw, gap = 120, 340, 60
    y0 = 170
    for i, (t, desc, color) in enumerate(cards):
        x = x0 + i * (bw + gap)
        rrect(d, [x, y0, x + bw, y0 + 220], 20, (255, 255, 255),
              outline=color, width=3)
        text_center(d, x + bw / 2, y0 + 30, t, fb(32), INK)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + bw / 2, y0 + 90 + j * 38, line, fr(24), SUB)
        if i < 2:
            arrow(d, x + bw + 8, y0 + 110, x + bw + gap - 8, y0 + 110,
                  fill=(148, 163, 184), width=4)

    rrect(d, [120, 470, 1280, 620], 18, (255, 251, 240), outline=WARN, width=2)
    text_center(d, 700, 496, "예방: 숫자가 들어가는 기능은 손으로 계산해 대조한다", fb(26), INK)
    text_center(d, 700, 544, "명세서에 계산식과 예시 값을 함께 적어 두면 환각이 줄어든다",
                fr(24), SUB)

    img.save(os.path.join(ASSETS, "fig-failure-1.png"))
    print("fig-failure-1.png saved")


# ------------------------------------------------- fig-failure-2: 보안 구멍
def make_failure_2():
    W, H = 1400, 700
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "실패 패턴 2: 보안 구멍", fb(40), INK)
    text_center(d, W / 2, 78, "겉은 멀쩡하지만, 문이 열려 있다",
                fr(26), SUB)

    holes = [
        ("API 키 노출", "코드에 키를\n그대로 적어둠", RED),
        ("인증 우회", "주소만 알면\n누구나 관리자 화면", RED),
        ("DB 규칙 없음", "읽기·쓰기 제한\n설정이 비어 있음", WARN),
    ]
    x0, bw, gap = 120, 340, 60
    y0 = 170
    for i, (t, desc, color) in enumerate(holes):
        x = x0 + i * (bw + gap)
        rrect(d, [x, y0, x + bw, y0 + 220], 20, (255, 255, 255),
              outline=color, width=3)
        text_center(d, x + bw / 2, y0 + 30, t, fb(30), INK)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + bw / 2, y0 + 90 + j * 38, line, fr(24), SUB)

    rrect(d, [120, 470, 1280, 620], 18, (255, 245, 244), outline=RED, width=2)
    text_center(d, 700, 496, "예방: 배포 전 보안 3점만 확인한다", fb(26), INK)
    text_center(d, 700, 544, "키 분리 · 로그인 없는 민감 화면 금지 · DB 접근 규칙 설정",
                fr(24), SUB)

    img.save(os.path.join(ASSETS, "fig-failure-2.png"))
    print("fig-failure-2.png saved")


# ------------------------------------------------- fig-failure-3: 유지보수 부채
def make_failure_3():
    W, H = 1400, 700
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "실패 패턴 3: 유지보수 부채", fb(40), INK)
    text_center(d, W / 2, 78, "오늘은 되지만, 다음 달에는 못 고친다",
                fr(26), SUB)

    stages = [
        ("1주차", "빠르게 완성\n기분 최고", TEAL),
        ("1개월 후", "고치려니 엉킴\n파일이 30개", WARN),
        ("3개월 후", "아무도 못 만짐\n처음부터 다시", RED),
    ]
    x0, bw, gap = 120, 340, 60
    y0 = 170
    for i, (t, desc, color) in enumerate(stages):
        x = x0 + i * (bw + gap)
        rrect(d, [x, y0, x + bw, y0 + 220], 20, (255, 255, 255),
              outline=color, width=3)
        text_center(d, x + bw / 2, y0 + 30, t, fb(30), INK)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + bw / 2, y0 + 90 + j * 38, line, fr(24), SUB)
        if i < 2:
            arrow(d, x + bw + 8, y0 + 110, x + bw + gap - 8, y0 + 110,
                  fill=(148, 163, 184), width=4)

    rrect(d, [120, 470, 1280, 620], 18, (238, 251, 253), outline=TEAL, width=2)
    text_center(d, 700, 496, "예방: 구조를 물을 때마다 물어본다", fb(26), INK)
    text_center(d, 700, 544, "\"같은 기능끼리 모아줘\" \"파일 이름을 역할대로 바꿔줘\" — 작은 정리 요청이 부채를 막는다",
                fr(24), SUB)

    img.save(os.path.join(ASSETS, "fig-failure-3.png"))
    print("fig-failure-3.png saved")


# ------------------------------------------------- fig-spec-template: 명세서 구조도
def make_spec_template():
    W, H = 1500, 760
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "AI가 이해하는 명세서의 5요소", fb(40), INK)
    text_center(d, W / 2, 78, "이 순서대로 적으면 AI가 덜 틀린다",
                fr(26), SUB)

    rrect(d, [500, 160, 1000, 260], 20, (30, 41, 59))
    text_center(d, 750, 184, "1. 목적", fb(34), WHITE)
    text_center(d, 750, 226, "이 서비스를 왜 만드는가, 한 문장", fr(24), (203, 213, 225))

    items = [
        ("2. 사용자", "누가, 무엇을 하러 오는가", BLUE, 320),
        ("3. 화면 목록", "화면 이름과 각 화면의 역할", TEAL, 440),
        ("4. 데이터 항목", "모으는 정보와 형식·필수 여부", CORAL, 560),
        ("5. 예외 상황", "잘못됐을 때의 동작과 메시지", PURPLE, 680),
    ]
    for t, desc, color, y in items:
        rrect(d, [500, y - 40, 1000, y + 40], 16, (255, 255, 255),
              outline=color, width=3)
        d.ellipse([540, y - 24, 588, y + 24], fill=color)
        fnum = fb(26)
        num = t.split(".")[0]
        bb = d.textbbox((0, 0), num, font=fnum)
        d.text((564 - (bb[2] - bb[0]) / 2 - bb[0], y - 20), num, font=fnum, fill=(255, 255, 255))
        d.text((610, y - 26), t.split(". ", 1)[1], font=fb(28), fill=INK)
        d.text((610, y + 8), desc, font=fr(22), fill=SUB)
        arrow(d, 750, y - 45, 750, y - 40 + 0, fill=(148, 163, 184), width=0)

    text_center(d, 750, 730, "템플릿은 21장에서 복사해 바로 쓴다",
                fr(24), SUB)
    img.save(os.path.join(ASSETS, "fig-spec-template.png"))
    print("fig-spec-template.png saved")


# ------------------------------------------------- fig-small-tasks: 작은 단위 분할
def make_small_tasks():
    W, H = 1500, 700
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "큰 요청 하나 vs 작은 요청 여섯 개", fb(40), INK)
    text_center(d, W / 2, 78, "나눌수록 고치기 쉬워진다",
                fr(26), SUB)

    rrect(d, [60, 150, 700, 600], 20, (255, 255, 255), outline=CARD_LINE, width=2)
    text_center(d, 380, 172, "나쁜 예: 한 번에 다", fb(30), RED)
    rrect(d, [120, 240, 640, 340], 14, (255, 240, 240), outline=RED, width=2)
    for j, line in enumerate(["\"카페 메뉴판 사이트를", "멋지게 만들어줘\""]):
        text_center(d, 380, 266 + j * 36, line, fr(26), INK)
    arrow(d, 380, 360, 380, 400, fill=RED, width=4)
    text_center(d, 380, 420, "어디가 틀렸는지 모른다", fr(24), SUB)
    text_center(d, 380, 458, "되돌리기도 어렵다", fr(24), SUB)
    text_center(d, 380, 530, "문맥 한계로 중간부터 엉킨다", fr(24), SUB)

    rrect(d, [800, 150, 1440, 600], 20, (255, 255, 255), outline=TEAL, width=3)
    text_center(d, 1120, 172, "좋은 예: 한 번에 하나씩", fb(30), (20, 120, 110))
    steps = [
        "1. 빈 화면 틀 만들기",
        "2. 메뉴 목록 화면",
        "3. 메뉴 상세 화면",
        "4. 주문 담기 기능",
        "5. 주문서 화면",
        "6. 디자인 다듬기",
    ]
    y = 230
    for s in steps:
        rrect(d, [880, y, 1360, y + 52], 12, (240, 252, 250), outline=TEAL, width=1)
        d.text((910, y + 13), s, font=fr(24), fill=INK)
        if y < 230 + 5 * 62:
            arrow(d, 1120, y + 56, 1120, y + 62, fill=TEAL, width=3)
        y += 62
    text_center(d, 1120, 560, "틀리면 그 단계만 다시", fr(22), SUB)

    img.save(os.path.join(ASSETS, "fig-small-tasks.png"))
    print("fig-small-tasks.png saved")


# ------------------------------------------------- fig-debug-flow: 디버깅 대화 흐름
def make_debug_flow():
    W, H = 1500, 720
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "디버깅 대화의 흐름", fb(40), INK)
    text_center(d, W / 2, 78, "증상을 설명하면, AI가 원인을 찾는다",
                fr(26), SUB)

    steps = [
        ("1. 증상 정리", "한 일 · 기대 결과\n실제 결과 · 오류 메시지", CORAL),
        ("2. 원인 질문", "\"왜 이런지 설명하고\n고쳐줘\"", BLUE),
        ("3. 실행 확인", "바뀐 화면을\n눈으로 직접 확인", TEAL),
        ("4. 범위 좁히기", "3번 반복되면\n요청을 더 작게", WARN),
    ]
    x0, bw, gap = 60, 320, 30
    y0 = 170
    for i, (t, desc, color) in enumerate(steps):
        x = x0 + i * (bw + gap)
        rrect(d, [x, y0, x + bw, y0 + 230], 20, (255, 255, 255),
              outline=color, width=3)
        d.rectangle([x, y0, x + bw, y0 + 12], fill=color)
        text_center(d, x + bw / 2, y0 + 34, t, fb(28), INK)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + bw / 2, y0 + 84 + j * 38, line, fr(23), SUB)
        if i < 3:
            arrow(d, x + bw + 5, y0 + 115, x + bw + gap - 5, y0 + 115,
                  fill=(148, 163, 184), width=5)

    arrow(d, 1250, 400, 250, 400, fill=TEAL, width=3)
    text_center(d, 750, 430, "안 되면 1번으로 돌아가 증상을 다시 적는다 (같은 말 반복 금지)", fr(24), TEAL)

    rrect(d, [60, 520, 1440, 650], 18, (30, 41, 59))
    text_center(d, 750, 544, "금지 문장: \"안 돼\" \"이상해\" \"다시 해줘\"", fb(26), CORAL)
    text_center(d, 750, 588, "대신: 무엇이, 어떻게, 어디서 틀렸는지를 구체적으로",
                fr(24), (203, 213, 225))

    img.save(os.path.join(ASSETS, "fig-debug-flow.png"))
    print("fig-debug-flow.png saved")


# ------------------------------------------------- fig-deploy-flow: 배포 흐름도
def make_deploy_flow():
    W, H = 1500, 700
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "무료 호스팅 배포의 흐름", fb(40), INK)
    text_center(d, W / 2, 78, "GitHub에 올리면, 호스팅이 자동으로 받아간다",
                fr(26), SUB)

    steps = [
        ("1. AI로 만들기", "빌더·에이전트로\n화면 완성", CORAL),
        ("2. GitHub 저장", "파일을 웹에서\n업로드·커밋", BLUE),
        ("3. 호스팅 연결", "Vercel·Netlify 등에\n저장소 연결", TEAL),
        ("4. 주소 받기", "공개 URL 발급\n지인에게 공유", PURPLE),
    ]
    x0, bw, gap = 60, 320, 30
    y0 = 170
    for i, (t, desc, color) in enumerate(steps):
        x = x0 + i * (bw + gap)
        rrect(d, [x, y0, x + bw, y0 + 220], 20, (255, 255, 255),
              outline=color, width=3)
        d.rectangle([x, y0, x + bw, y0 + 12], fill=color)
        text_center(d, x + bw / 2, y0 + 34, t, fb(28), INK)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + bw / 2, y0 + 84 + j * 38, line, fr(24), SUB)
        if i < 3:
            arrow(d, x + bw + 5, y0 + 110, x + bw + gap - 5, y0 + 110,
                  fill=(148, 163, 184), width=5)

    rrect(d, [60, 470, 1440, 620], 18, (240, 252, 250), outline=TEAL, width=2)
    text_center(d, 750, 496, "고치면 GitHub에만 다시 올리면 된다", fb(26), INK)
    text_center(d, 750, 544, "호스팅이 변경을 감지해 자동으로 다시 배포한다 — 수동 업로드 불필요",
                fr(24), SUB)

    img.save(os.path.join(ASSETS, "fig-deploy-flow.png"))
    print("fig-deploy-flow.png saved")


# ------------------------------------------------- fig-maintenance: 최소 관리 루틴
def make_maintenance():
    W, H = 1500, 700
    img = Image.new("RGB", (W, H), LIGHT_BG)
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "월 30분 최소 관리 루틴", fb(40), INK)
    text_center(d, W / 2, 78, "매주 한 번, 이 네 가지만 확인한다",
                fr(26), SUB)

    items = [
        ("살아있는지", "주소를 열어\n화면이 뜨는지", TEAL),
        ("오류 알림", "호스팅·메일의\n오류 보고 확인", WARN),
        ("백업 존재", "GitHub에 최신\n파일이 있는지", BLUE),
        ("비용 확인", "크레딧·요금제\n잔량과 청구서", CORAL),
    ]
    x0, bw, gap = 60, 320, 30
    y0 = 170
    for i, (t, desc, color) in enumerate(items):
        x = x0 + i * (bw + gap)
        rrect(d, [x, y0, x + bw, y0 + 210], 20, (255, 255, 255),
              outline=color, width=3)
        d.rectangle([x, y0, x + bw, y0 + 12], fill=color)
        text_center(d, x + bw / 2, y0 + 34, t, fb(30), INK)
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + bw / 2, y0 + 84 + j * 38, line, fr(24), SUB)

    rrect(d, [60, 470, 1440, 610], 18, (30, 41, 59))
    text_center(d, 750, 496, "이상 없으면 끝 — 건드리지 않는 것이 최선", fb(28), CORAL)
    text_center(d, 750, 544, "문제가 생겼을 때만 31장의 디버깅 대화법으로 고친 뒤, GitHub에 다시 저장한다",
                fr(24), (203, 213, 225))

    img.save(os.path.join(ASSETS, "fig-maintenance.png"))
    print("fig-maintenance.png saved")


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    make_cover()
    make_vs_dev()
    make_failure_1()
    make_failure_2()
    make_failure_3()
    make_spec_template()
    make_small_tasks()
    make_debug_flow()
    make_deploy_flow()
    make_maintenance()
