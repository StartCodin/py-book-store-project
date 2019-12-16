from src.reader import *
from src.store import *
from src.staff import *
from src.book import *

store = Store('Readers\' Paradise')

anna_karenina = Book('Anna Karenina', 'Novel', 900, 34,
                     'Leo Tolstoy', 'Vintage Books', 1500)

compilers = Book('Compilers: Principles, Techniques, and Tools',
                 'Textbook', 1040, 2, 'Alfred Al Aho, et al', 'Pearson', 400)

front_dek_operator = Staff('Front Desk Operator', 'Mysuru')

vijay = Reader('Vijay Kumar', 'Bengaluru', 'vijay@domain.com', '9000080000')
malini = Reader('Malini Sharma', 'Chennai', 'malini@domain.com', '9000080000')
ramakrishna = Reader('Ramakrishna Babu', 'Hyderabad',
                     'ramakrishna@domain.com', '9000080000')
giri = Reader('Giridhar', 'Bidar', 'giri@domain.com', '9000080000')

anna_karenina.register(front_dek_operator)
compilers.register(front_dek_operator)

store.add_book(anna_karenina)
store.add_book(compilers)

store.add_interested_reader(anna_karenina, malini)
store.add_interested_reader(anna_karenina, giri)
store.add_interested_reader(compilers, malini)

vijay_receipt_id = store.buy_book(anna_karenina, vijay, front_dek_operator)
rk_receipt_id = store.buy_book(compilers, ramakrishna, front_dek_operator)

store.print_receipt(vijay_receipt_id)
store.print_receipt(rk_receipt_id)
