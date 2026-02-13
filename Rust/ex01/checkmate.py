def checkmate(board_str: str) -> str:
    # 1. Validation & Parsing
    if not board_str or not board_str.strip():
        return "Error"
    
    lines = [line.strip() for line in board_str.strip().split('\n') if line.strip()]
    if not lines:
        return "Error"
    
    size = len(lines)
    if any(len(line) != size for line in lines):
        return "Error"


    # 2. Find King Positions (นับและเช็กจำนวน King)
    # สร้าง List ของพิกัด (r, c) ทั้งหมดที่เจอ 'K'
    k_positions = [(r, c) for r, row in enumerate(lines) 
                for c, char in enumerate(row) if char == 'K']

# ตรวจสอบว่าต้องมี King เพียงตัวเดียวเท่านั้น
    if len(k_positions) != 1:
        return "Error"  

# ดึงพิกัดของ King ตัวเดียวที่มีอยู่มาใช้งาน
    kr, kc = k_positions[0]

    # 3. Define Attack Patterns
    # ทิศทาง: (delta_row, delta_col) -> ชิ้นส่วนที่อันตรายในทิศนั้น
    directions = {
        "straight": [(-1, 0), (1, 0), (0, -1), (0, 1)],  # R, Q
        "diagonal": [(-1, -1), (-1, 1), (1, -1), (1, 1)] # B, Q
    }

    # Check Ray Casting (R, B, Q)
    for move_type, moves in directions.items():
        dangerous_pieces = {'R', 'Q'} if move_type == "straight" else {'B', 'Q'}
        for dr, dc in moves:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                piece = lines[r][c]
                if piece != '.':
                    if piece in dangerous_pieces:
                        return "Success"
                    break # เจอหมากตัวอื่นขวาง
                r, c = r + dr, c + dc

    # 4. Check Pawn (P) - หมากรุกปกติเบี้ยกินเฉียงขึ้น 
    # ในโจทย์นี้ถ้า King ต้องระวัง P แสดงว่า P ต้องอยู่แถว "ถัดลงมา" (kr + 1)
    for dc in [-1, 1]:
        pr, pc = kr + 1, kc + dc
        if 0 <= pr < size and 0 <= pc < size:
            if lines[pr][pc] == 'P':
                return "Success"

    return "Fail"