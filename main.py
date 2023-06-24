def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    m_count = int(input('Enter the number of males: '))
    f_count = int(input('Enter the number of females: '))

    total_students = m_count + f_count
    m_perc = (m_count / total_students) * 100
    f_perc = (f_count / total_students) * 100

    print('The total number of students:', total_students)
    print('The number of males and females:', m_count, f_count)
    print(f'The percentage of males and females: {m_perc:.2f}%\t{f_perc:.2f}%')


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
