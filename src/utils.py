
class CostCalculator:
    '''
    Класс для расчета стоимости вызова LLM.
    Изолирует логику расчетов от API вызовов.
    '''
    def __init__(self, price_per_1k_tokens: float):
        if price_per_1k_tokens < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price_per_1k = price_per_1k_tokens

    def calculate_call_cost(self, output_tokens: int) -> float:
        '''
        Рассчитывает стоимость одного вызова.
        '''
        cost = (output_tokens / 1000) * self.price_per_1k
        return round(cost, 5)

    def calculate_monthly_tco(self, calls_per_day: int, avg_tokens: int) -> float:
        '''
        Рассчитывает совокупную стоимость владения (TCO) за месяц.
        '''
        daily_cost = self.calculate_call_cost(avg_tokens) * calls_per_day
        return round(daily_cost * 30, 2)
