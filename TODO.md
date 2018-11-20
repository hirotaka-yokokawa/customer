TODO

---------------------
[x]B-1
[x]ken = Customer(first_name="Ken", family_name="Tanaka")
[x]tom = Customer(first_name="Tom", family_name="Ford").full_name()
[x]tom.full_name()  # "Tom Ford" という値を返す
[x]ken.full_name()  # "Ken Tanaka" という値を返す

[x]B-2
[x]ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
[x]ken.age  # 15 という値を返す
[x]tom = Customer(first_name="Tom", family_name="Ford", age= 57)
[x]tom.age # 57 という値を返す
[x]ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
[x]ieyasu.age # 73 という値を返す

[]B-3
[]ken.entry_fee()  # 1000 という値を返す
[]tom.entry_fee() # 1500 という値を返す
[]ieyasu.entry_fee() # 1200 という値を返す
#料金の計算ルール
こども料金(20歳未満): 1000円
おとな料金(20歳以上65歳未満): 1500円
シニア料金(65歳以上): 1200円