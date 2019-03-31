# -*- coding: utf-8 -*-


def total(selling_price, down_payments_ratio=0.1, month_pay_raito=0.05):
    """总价"""
    # 分期总金额
    installment_amount = selling_price * (1 - down_payments_ratio) + 0.12 * selling_price
    months = int(1 / month_pay_raito)
    month_principal = installment_amount * month_pay_raito
    infos = []
    for month in range(1, months + 1):
        infos.append({
            "month": month,
            "total_arrears": installment_amount - (month - 1) * month_principal,
            "month_interest": (installment_amount - (month - 1) * month_principal) * 0.12 / 12,
            "month_principal": month_principal,
            "month_pay": (installment_amount - (month - 1) * month_principal) * 0.12 / 12 + month_principal,
            "next_total": installment_amount - month * month_principal
        })
    return infos


if __name__ == '__main__':
    infos = total(100)
    for info in infos:
        print(info)
    print(sum([info["month_pay"] for info in infos]))
