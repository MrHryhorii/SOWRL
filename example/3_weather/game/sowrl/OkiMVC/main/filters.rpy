transform red_blue_tint:
    matrixcolor TintMatrix("#f00")
    linear 3.0 matrixcolor TintMatrix("#00f")
    linear 3.0 matrixcolor TintMatrix("#f00")
    repeat

transform swap_red_and_green:
    matrixcolor Matrix([ 0.0, 1.0, 0.0, 0.0,
                         1.0, 0.0, 0.0, 0.0,
                         0.0, 0.0, 1.0, 0.0,
                         0.0, 0.0, 0.0, 1.0, ])

transform okiflip:
    xalign 0.5 yalign 0.5 rotate 180
    
transform invertcolors:
    matrixcolor InvertMatrix()

transform identitycolors:
    matrixcolor IdentityMatrix()

transform hit2:
    matrixcolor TintMatrix("#FFF") ## FFF is effectively no tint
    linear 1.0 matrixcolor TintMatrix("#F00")
    linear 0.5 matrixcolor TintMatrix("#FFF")

transform anim2:
    
    linear 3.0 matrixcolor Matrix([ -1.0, 0.0, 0.0, 1.0,
                                    0.0, -1.0, 0.0, 1.0,
                                    0.0, 0.0, -1.0, 1.0,
                                    0.0, 0.0, 0.0, 1.0, ])

transform anim3:
    matrixcolor OkiColorMatrix([ -1.0, 0.0, 0.0, 1.0,
                                    0.0, -1.0, 0.0, 1.0,
                                    0.0, 0.0, -1.0, 1.0,
                                    0.0, 0.0, 0.0, 1.0, ])

    linear 1.0 matrixcolor OkiColorMatrix([ 0.0, 1.0, 0.0, 0.0,
                                            1.0, 0.0, 0.0, 0.0,
                                            0.0, 0.0, 1.0, 0.0,
                                            0.0, 0.0, 0.0, 1.0, ])

transform anim:
    matrixcolor OkiColorMatrix(IdentityMatrix())
    linear 5.0 matrixcolor OkiColorMatrix(InvertMatrix())
    
  
    

    
            
