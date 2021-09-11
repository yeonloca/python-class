def bmi_weight(height,gender):
       
       if gender=="남자":
              print("키",height,"cm의 표준 체중은",round(height/100*height/100*22,2),"입니다.")
       elif gender=="여자":
              print("키",height,"cm의 표준 체중은",round(height/100*height/100*21,2),"입니다.")
