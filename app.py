import tkinter as tk
from tkinter import messagebox

# 1. 단어 데이터베이스 (단어: {뜻, 예문})
WORD_DICT = {
    "apple": {
        "meaning": "사과",
        "sentence": "I ate a delicious apple for breakfast."
    },
    "banana": {
        "meaning": "바나나",
        "sentence": "Monkeys love to eat banana."
    },
    "computer": {
        "meaning": "컴퓨터",
        "sentence": "I use a computer to learn programming."
    }
}

def search_word():
    # 입력한 단어 가져오기 (소문자 변환)
    target_word = entry.get().strip().lower()
    
    if not target_word:
        messagebox.showwarning("경고", "영단어를 입력해 주세요.")
        return

    # Text 위젯 수정 가능 상태로 변경 및 기존 내용 삭제
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)

    if target_word in WORD_DICT:
        data = WORD_DICT[target_word]
        meaning = data["meaning"]
        sentence = data["sentence"]

        # 뜻 출력
        result_text.insert(tk.END, f"📌 뜻: {meaning}\n\n")
        
        # 예문 출력 시작 위치 기록
        result_text.insert(tk.END, "📝 예문: ")
        
        # 예문 내에서 검색 단어 위치 찾기 및 빨간색 강조 처리
        sentence_lower = sentence.lower()
        start_idx = 0
        
        while True:
            # 단어가 나타나는 위치 찾기
            found_pos = sentence_lower.find(target_word, start_idx)
            if found_pos == -1:
                # 더 이상 단어가 없으면 남은 문장 출력 후 종료
                result_text.insert(tk.END, sentence[start_idx:])
                break
            
            # 단어 앞 부분 출력
            result_text.insert(tk.END, sentence[start_idx:found_pos])
            
            # 검색 단어 부분 출력 (빨간색 태그 적용)
            actual_word = sentence[found_pos:found_pos + len(target_word)]
            result_text.insert(tk.END, actual_word, "highlight")
            
            # 다음 검색 위치 업데이트
            start_idx = found_pos + len(target_word)
            
    else:
        result_text.insert(tk.END, "사전에 등록되지 않은 단어입니다.")

    # 다시 수정 불가능 상태로 변경
    result_text.config(state=tk.DISABLED)

# --- GUI 화면 구성 ---
root = tk.Tk()
root.title("나만의 영단어장")
root.geometry("450 x 350")

# 입력창 레이아웃
frame_input = tk.Frame(root)
frame_input.pack(pady=15)

label = tk.Label(frame_input, text="영단어 입력: ", font=("맑은 고딕", 11))
label.pack(side=tk.LEFT)

entry = tk.Entry(frame_input, font=("맑은 고딕", 11), width=18)
entry.pack(side=tk.LEFT, padx=5)
# 엔터키를 눌러도 검색 가능하도록 설정
entry.bind("<Return>", lambda event: search_word())

btn_search = tk.Button(frame_input, text="검색", font=("맑은 고딕", 10), command=search_word)
btn_search.pack(side=tk.LEFT)

# 결과 출력창 (Text 위젯)
result_text = tk.Text(root, font=("맑은 고딕", 11), wrap=tk.WORD, width=45, height=10)
result_text.pack(padx=15, pady=10)

# 핵심: 빨간색 강조를 위한 태그(Tag) 설정
result_text.tag_config("highlight", foreground="red", font=("맑은 고딕", 11, "bold"))

# 초기에는 수정할 수 없도록 설정
result_text.config(state=tk.DISABLED)

root.mainloop()
