from django.shortcuts import render

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def input_page(request):
    return render(request, 'primes/input_page.html')

def output_page(request):
    number = request.GET.get('number')
    if number is not None:
        number = int(number)
        primes = [n for n in range(2, number + 1) if is_prime(n)]
    else:
        primes = []
        number = 0
    return render(request, 'primes/output_page.html', {'primes': primes, 'number': number})
 