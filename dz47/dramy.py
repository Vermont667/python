from dramy_list import Drams


def main():
    for i in range(1, 10):
        dram = Drams(f'https://kdramy.online/bl-lakorny/page/{i}/', 'what_to_see.txt')
        dram.run()


if __name__ == '__main__':
    main()
