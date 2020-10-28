local x::Int
local x1::Int
local y2::Int
local y::Int
x = 5
x1 = 0
y2 = 10
y = readline()
while (x1 < y) || (x1 == y)
    if x1 < 3
        println(2)
    elseif x1 == 3
        println(20)
    elseif x1 == 4
        println(200)
    else
        println(2000)
    end

    if (x1 > 3) && (y2 == 10)
        println(10)
    else
        println(100)
    end

    println((x1 > 3) && (x1 < y2))
    println(x1)
    x1 = x1 + 1
end
