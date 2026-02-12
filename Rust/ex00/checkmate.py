def checkmate(board):
    if not board or not board.strip():
        return
    
    lines = [line for line in board.split('\n') if line]
    if not lines:
        return

    size = len(lines)
    for line in lines:
        if len(line) != size:
            return

    # find King (K) 
    k_pos = None
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                k_pos = (r, c)
                break
        if k_pos: break
            
    if not k_pos:
        return

    kr, kc = k_pos

    # 3. Ray Casting attack check (R, B, Q) 
    # The piece captures the first possible piece in its path
    def is_attacked(dr, dc, attackers):
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece != '.':
                return piece in attackers
            r += dr
            c += dc
        return False


    # check line R, Q
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if is_attacked(dr, dc, ['R', 'Q']):
            print("Success")
            return

    # check diagonal B, Q
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if is_attacked(dr, dc, ['B', 'Q']):
            print("Success")
            return

    # check Pawn 'P' 
    # King เบี้ยที่รุกได้ต้องอยู่แถว "ถัดลงมา" (kr + 1) 
    for dc in [-1, 1]:
        pr, pc = kr + 1, kc + dc
        if 0 <= pr < size and 0 <= pc < size:
            if lines[pr][pc] == 'P':
                print("Success")
                return

    # หากไม่มีหมากตัวไหนรุก King ได้ 
    print("Fail")