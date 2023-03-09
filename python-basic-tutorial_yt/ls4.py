#賛否両論コード

# ex.1

# 網羅的・可読性向上
def level_up_1(exp, level): 
    if exp >= 100:
        level += 1
    else:
        level = level
    return level

# コードがすっきりする
def level_up_2(exp, level):
    if exp >= 100:
        level += 1
    return level


# ex.2
def level_up_3(exp, level):
    if exp >= 100:
        level += 1 # 再代入を許すべきか or
        new_level = level + 1 #もしくはこうする
    return level


# ex.3

# ロジックがすっきり・ネストが浅くなる。だが、網羅的ではない
def level_up_4(exp, level, x, y):
    if exp < 100:
        return # 早期リターン

    if exp >= 100 and y >= 100:
        new_level = level + 3
    elif x >= 50 and y >=50:
        new_level = level + 2
    else:
        new_level = level + 1
    
    update_table('user', cols={'level': new_level})

# elseを使ってあげることで網羅的に
def level_up_5(exp, level, x, y):
    if exp < 100:
        return # 早期リターン
    else: 
        if exp >= 100 and y >= 100:
            new_level = level + 3
        elif x >= 50 and y >=50:
            new_level = level + 2
        else:
            new_level = level + 1
    
    update_table('user', cols={'level': new_level})


# ex.4 タイプアノテーションはつけるべきか

# 型を意識したコーディングがしやすい。一方、静的型付け言語を使えば良いのではという意見も
def level_up_6(exp: int, level: int) -> int:
    if exp >= 100:
        level += 1
    return level