def refresh_all(window, list, type):
    if len(list) == 0:
        list = ['No Addresses Available']

    if type == 'addresses':
        window.comboBox_5.clear()
        window.comboBox_5.addItems(list)
        window.addr_combo.clear()
        window.addr_combo.addItems(list)
        window.comboBox_4.clear()
        window.comboBox_4.addItems(list)
        window.fld_to_box.clear()
        window.fld_to_box.addItems(list)
        window.comboBox_3.clear()
        window.comboBox_3.addItems(list)      

    elif type == 'multisig':
        window.comboBox_2.clear()
        window.comboBox_2.addItems(list)

    elif type == 'all':
        window.pay_to_combo_box.clear()
        window.pay_to_combo_box.addItems(list)

    elif type == 'balances':
        list = [item for item in list if not (item[0]=='P' or (item[0:3] =='pkt' and len(item)>61))]
        window.fld_frm_box.clear()
        window.fld_frm_box.addItems(list)
        window.pay_from_combo_box.clear()
        window.pay_from_combo_box.addItems(list)
