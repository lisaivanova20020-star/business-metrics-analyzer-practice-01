
import pandas as pd


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100


def main():
    # Данные предприятия за три месяца
    data = {
        "Месяц": ["Январь", "Февраль", "Март"],
        "Выручка": [120000, 150000, 135000],
        "Затраты": [80000, 100000, 90000],
    }

    # Создание таблицы
    df = pd.DataFrame(data)

    # Расчёт прибыли
    df["Прибыль"] = df["Выручка"] - df["Затраты"]

    print("BUSINESS METRICS ANALYZER")
    print("=" * 45)

    print("\nПоказатели предприятия:")
    print(df.to_string(index=False))

    # Средняя выручка
    average_revenue = df["Выручка"].mean()
    print(f"\nСредняя выручка: {average_revenue:.2f} руб.")

    # Расчёт рентабельности за каждый месяц
    print("\nРентабельность по месяцам:")

    for _, row in df.iterrows():
        profitability = calculate_profitability(
            row["Выручка"],
            row["Затраты"]
        )
        print(f"{row['Месяц']}: {profitability:.2f}%")

    # Общая рентабельность
    total_revenue = df["Выручка"].sum()
    total_cost = df["Затраты"].sum()

    total_profitability = calculate_profitability(
        total_revenue,
        total_cost
    )

    print(f"\nОбщая рентабельность: {total_profitability:.2f}%")


if __name__ == "__main__":
    main()

