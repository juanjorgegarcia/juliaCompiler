function soma(x::Int)::Int
    local test::Int
    local a::Int
    a = x + 1
    println(a)
    if a < 5
        a = soma(a)
    end
    return a
end
local a::Int
a = 1
a = soma(a)
println(a)
