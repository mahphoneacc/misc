# Нахождение среднего
def mean(in_list):
    return sum(in_list) / len(in_list)

# Нахождение дисперсии
def variance(in_list):
    mean = sum(in_list) / len(in_list)
    square_dev_list = [(i - mean)**2 for i in in_list]
    return sum(square_dev_list) / (len(square_dev_list) - 1)

# Нахождение стандартного отклонения
def stand_dev(in_list):
    mean = sum(in_list) / len(in_list)
    square_dev_list = [(i - mean)**2 for i in in_list]
    D = sum(square_dev_list) / (len(square_dev_list) - 1)
    return D**0.5

# Нахождение стандартизированного списка
def z_scores(in_list):
    mean = sum(in_list) / len(in_list)
    square_dev_list = [(i - mean)**2 for i in in_list]
    D = sum(square_dev_list) / (len(square_dev_list) - 1)
    sigma = D**0.5
    res = [(i - mean) / sigma for i in in_list]
    return res
	
# Нахождение стандартной ошибки среднего
def standard_error(in_list):
	sd = stand_dev(in_list)
	return sd / (len(in_list)**0.5)

# Показать основные стат метрики списка
def show_list_stat(in_list):
	print('N = ', len(in_list))
	print('Mean = ', mean(in_list))
	print('Variance = ', variance(in_list))
	print('Std Dev = ', stand_dev(in_list))
	print('Std Err = ', standard_error(in_list))

# Коэффициент ковариации	
def covar(in_list1, in_list2):
	mean1 = sum(in_list1) / len(in_list1)
	mean2 = sum(in_list2) / len(in_list2)
	leng = min(len(in_list1), len(in_list2))
	summ = 0
	for i in range(leng):
		summ += (in_list1[i] - mean1) * (in_list2[i] - mean2)
	sd_1 = stand_dev(in_list1)
	sd_2 = stand_dev(in_list2)
	# Ковариация
	cov = summ / (leng - 1)
	print('covar: ', str(cov))
	# Коэффициент корелляции (Пирсона)
	r_xy = cov / sd_1 / sd_2
	print('pearsonr: ', str(r_xy))
	# R**2 Коэффициент детерминации (Общая дисперсия) 
	print('shared variance: ', str(r_xy**2))
	# Нахождение коэффициентов регрессионной прямой, при зависимой второй переменной
	sum_1 = sum(in_list1)
	sum_2 = sum(in_list2)
	sum_sq_1 = sum(in_list1 * in_list1)		# Сумма квадратов списка 1
	sum_12 = sum(in_list1 * in_list2)		# Сумма произведений списка 1 и списка 2
	koef_a = (sum_12 - mean2 * sum_1) / (sum_sq_1 - mean1 * sum_1)
	koef_b = (mean2 * sum_sq_1 - mean1 * sum_12) / (sum_sq_1 - mean1 * sum_1)
	print('y = ', koef_b, '+', koef_a, 'x')

	
	
	
	
	