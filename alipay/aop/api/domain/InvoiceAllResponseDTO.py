#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.InvoiceLineResponseDTO import InvoiceLineResponseDTO
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class InvoiceAllResponseDTO(object):

    def __init__(self):
        self._attachment_name = None
        self._attachment_oss_key = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_inst_id = None
        self._buyer_invoice_title = None
        self._buyer_tax_no = None
        self._buyer_telephone = None
        self._exclude_tax_amt = None
        self._invoice_amt = None
        self._invoice_auth_date = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_line_list = None
        self._invoice_mail_status = None
        self._invoice_mail_status_name = None
        self._invoice_no = None
        self._invoice_note = None
        self._invoice_rcv_date = None
        self._invoice_status = None
        self._invoice_status_name = None
        self._invoice_type = None
        self._invoice_type_name = None
        self._is_red = None
        self._memo = None
        self._relevant_amt = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_company_name = None
        self._seller_custm_name = None
        self._seller_ip_role_id = None
        self._seller_mid = None
        self._seller_tax_no = None
        self._seller_telephone = None
        self._tax_amt = None

    @property
    def attachment_name(self):
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self._attachment_name = value
    @property
    def attachment_oss_key(self):
        return self._attachment_oss_key

    @attachment_oss_key.setter
    def attachment_oss_key(self, value):
        self._attachment_oss_key = value
    @property
    def buyer_address(self):
        return self._buyer_address

    @buyer_address.setter
    def buyer_address(self, value):
        self._buyer_address = value
    @property
    def buyer_bank_account(self):
        return self._buyer_bank_account

    @buyer_bank_account.setter
    def buyer_bank_account(self, value):
        self._buyer_bank_account = value
    @property
    def buyer_bank_name(self):
        return self._buyer_bank_name

    @buyer_bank_name.setter
    def buyer_bank_name(self, value):
        self._buyer_bank_name = value
    @property
    def buyer_inst_id(self):
        return self._buyer_inst_id

    @buyer_inst_id.setter
    def buyer_inst_id(self, value):
        self._buyer_inst_id = value
    @property
    def buyer_invoice_title(self):
        return self._buyer_invoice_title

    @buyer_invoice_title.setter
    def buyer_invoice_title(self, value):
        self._buyer_invoice_title = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def buyer_telephone(self):
        return self._buyer_telephone

    @buyer_telephone.setter
    def buyer_telephone(self, value):
        self._buyer_telephone = value
    @property
    def exclude_tax_amt(self):
        return self._exclude_tax_amt

    @exclude_tax_amt.setter
    def exclude_tax_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._exclude_tax_amt = value
        else:
            self._exclude_tax_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_amt = value
        else:
            self._invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_auth_date(self):
        return self._invoice_auth_date

    @invoice_auth_date.setter
    def invoice_auth_date(self, value):
        self._invoice_auth_date = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_line_list(self):
        return self._invoice_line_list

    @invoice_line_list.setter
    def invoice_line_list(self, value):
        if isinstance(value, list):
            self._invoice_line_list = list()
            for i in value:
                if isinstance(i, InvoiceLineResponseDTO):
                    self._invoice_line_list.append(i)
                else:
                    self._invoice_line_list.append(InvoiceLineResponseDTO.from_alipay_dict(i))
    @property
    def invoice_mail_status(self):
        return self._invoice_mail_status

    @invoice_mail_status.setter
    def invoice_mail_status(self, value):
        self._invoice_mail_status = value
    @property
    def invoice_mail_status_name(self):
        return self._invoice_mail_status_name

    @invoice_mail_status_name.setter
    def invoice_mail_status_name(self, value):
        self._invoice_mail_status_name = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
    @property
    def invoice_rcv_date(self):
        return self._invoice_rcv_date

    @invoice_rcv_date.setter
    def invoice_rcv_date(self, value):
        self._invoice_rcv_date = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def invoice_status_name(self):
        return self._invoice_status_name

    @invoice_status_name.setter
    def invoice_status_name(self, value):
        self._invoice_status_name = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def invoice_type_name(self):
        return self._invoice_type_name

    @invoice_type_name.setter
    def invoice_type_name(self, value):
        self._invoice_type_name = value
    @property
    def is_red(self):
        return self._is_red

    @is_red.setter
    def is_red(self, value):
        self._is_red = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def relevant_amt(self):
        return self._relevant_amt

    @relevant_amt.setter
    def relevant_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._relevant_amt = value
        else:
            self._relevant_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def seller_address(self):
        return self._seller_address

    @seller_address.setter
    def seller_address(self, value):
        self._seller_address = value
    @property
    def seller_bank_account(self):
        return self._seller_bank_account

    @seller_bank_account.setter
    def seller_bank_account(self, value):
        self._seller_bank_account = value
    @property
    def seller_bank_name(self):
        return self._seller_bank_name

    @seller_bank_name.setter
    def seller_bank_name(self, value):
        self._seller_bank_name = value
    @property
    def seller_company_name(self):
        return self._seller_company_name

    @seller_company_name.setter
    def seller_company_name(self, value):
        self._seller_company_name = value
    @property
    def seller_custm_name(self):
        return self._seller_custm_name

    @seller_custm_name.setter
    def seller_custm_name(self, value):
        self._seller_custm_name = value
    @property
    def seller_ip_role_id(self):
        return self._seller_ip_role_id

    @seller_ip_role_id.setter
    def seller_ip_role_id(self, value):
        self._seller_ip_role_id = value
    @property
    def seller_mid(self):
        return self._seller_mid

    @seller_mid.setter
    def seller_mid(self, value):
        self._seller_mid = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def seller_telephone(self):
        return self._seller_telephone

    @seller_telephone.setter
    def seller_telephone(self, value):
        self._seller_telephone = value
    @property
    def tax_amt(self):
        return self._tax_amt

    @tax_amt.setter
    def tax_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_amt = value
        else:
            self._tax_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_name:
            if hasattr(self.attachment_name, 'to_alipay_dict'):
                params['attachment_name'] = self.attachment_name.to_alipay_dict()
            else:
                params['attachment_name'] = self.attachment_name
        if self.attachment_oss_key:
            if hasattr(self.attachment_oss_key, 'to_alipay_dict'):
                params['attachment_oss_key'] = self.attachment_oss_key.to_alipay_dict()
            else:
                params['attachment_oss_key'] = self.attachment_oss_key
        if self.buyer_address:
            if hasattr(self.buyer_address, 'to_alipay_dict'):
                params['buyer_address'] = self.buyer_address.to_alipay_dict()
            else:
                params['buyer_address'] = self.buyer_address
        if self.buyer_bank_account:
            if hasattr(self.buyer_bank_account, 'to_alipay_dict'):
                params['buyer_bank_account'] = self.buyer_bank_account.to_alipay_dict()
            else:
                params['buyer_bank_account'] = self.buyer_bank_account
        if self.buyer_bank_name:
            if hasattr(self.buyer_bank_name, 'to_alipay_dict'):
                params['buyer_bank_name'] = self.buyer_bank_name.to_alipay_dict()
            else:
                params['buyer_bank_name'] = self.buyer_bank_name
        if self.buyer_inst_id:
            if hasattr(self.buyer_inst_id, 'to_alipay_dict'):
                params['buyer_inst_id'] = self.buyer_inst_id.to_alipay_dict()
            else:
                params['buyer_inst_id'] = self.buyer_inst_id
        if self.buyer_invoice_title:
            if hasattr(self.buyer_invoice_title, 'to_alipay_dict'):
                params['buyer_invoice_title'] = self.buyer_invoice_title.to_alipay_dict()
            else:
                params['buyer_invoice_title'] = self.buyer_invoice_title
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.buyer_telephone:
            if hasattr(self.buyer_telephone, 'to_alipay_dict'):
                params['buyer_telephone'] = self.buyer_telephone.to_alipay_dict()
            else:
                params['buyer_telephone'] = self.buyer_telephone
        if self.exclude_tax_amt:
            if hasattr(self.exclude_tax_amt, 'to_alipay_dict'):
                params['exclude_tax_amt'] = self.exclude_tax_amt.to_alipay_dict()
            else:
                params['exclude_tax_amt'] = self.exclude_tax_amt
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_auth_date:
            if hasattr(self.invoice_auth_date, 'to_alipay_dict'):
                params['invoice_auth_date'] = self.invoice_auth_date.to_alipay_dict()
            else:
                params['invoice_auth_date'] = self.invoice_auth_date
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_line_list:
            if isinstance(self.invoice_line_list, list):
                for i in range(0, len(self.invoice_line_list)):
                    element = self.invoice_line_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_line_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_line_list, 'to_alipay_dict'):
                params['invoice_line_list'] = self.invoice_line_list.to_alipay_dict()
            else:
                params['invoice_line_list'] = self.invoice_line_list
        if self.invoice_mail_status:
            if hasattr(self.invoice_mail_status, 'to_alipay_dict'):
                params['invoice_mail_status'] = self.invoice_mail_status.to_alipay_dict()
            else:
                params['invoice_mail_status'] = self.invoice_mail_status
        if self.invoice_mail_status_name:
            if hasattr(self.invoice_mail_status_name, 'to_alipay_dict'):
                params['invoice_mail_status_name'] = self.invoice_mail_status_name.to_alipay_dict()
            else:
                params['invoice_mail_status_name'] = self.invoice_mail_status_name
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
        if self.invoice_rcv_date:
            if hasattr(self.invoice_rcv_date, 'to_alipay_dict'):
                params['invoice_rcv_date'] = self.invoice_rcv_date.to_alipay_dict()
            else:
                params['invoice_rcv_date'] = self.invoice_rcv_date
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_status_name:
            if hasattr(self.invoice_status_name, 'to_alipay_dict'):
                params['invoice_status_name'] = self.invoice_status_name.to_alipay_dict()
            else:
                params['invoice_status_name'] = self.invoice_status_name
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.invoice_type_name:
            if hasattr(self.invoice_type_name, 'to_alipay_dict'):
                params['invoice_type_name'] = self.invoice_type_name.to_alipay_dict()
            else:
                params['invoice_type_name'] = self.invoice_type_name
        if self.is_red:
            if hasattr(self.is_red, 'to_alipay_dict'):
                params['is_red'] = self.is_red.to_alipay_dict()
            else:
                params['is_red'] = self.is_red
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.relevant_amt:
            if hasattr(self.relevant_amt, 'to_alipay_dict'):
                params['relevant_amt'] = self.relevant_amt.to_alipay_dict()
            else:
                params['relevant_amt'] = self.relevant_amt
        if self.seller_address:
            if hasattr(self.seller_address, 'to_alipay_dict'):
                params['seller_address'] = self.seller_address.to_alipay_dict()
            else:
                params['seller_address'] = self.seller_address
        if self.seller_bank_account:
            if hasattr(self.seller_bank_account, 'to_alipay_dict'):
                params['seller_bank_account'] = self.seller_bank_account.to_alipay_dict()
            else:
                params['seller_bank_account'] = self.seller_bank_account
        if self.seller_bank_name:
            if hasattr(self.seller_bank_name, 'to_alipay_dict'):
                params['seller_bank_name'] = self.seller_bank_name.to_alipay_dict()
            else:
                params['seller_bank_name'] = self.seller_bank_name
        if self.seller_company_name:
            if hasattr(self.seller_company_name, 'to_alipay_dict'):
                params['seller_company_name'] = self.seller_company_name.to_alipay_dict()
            else:
                params['seller_company_name'] = self.seller_company_name
        if self.seller_custm_name:
            if hasattr(self.seller_custm_name, 'to_alipay_dict'):
                params['seller_custm_name'] = self.seller_custm_name.to_alipay_dict()
            else:
                params['seller_custm_name'] = self.seller_custm_name
        if self.seller_ip_role_id:
            if hasattr(self.seller_ip_role_id, 'to_alipay_dict'):
                params['seller_ip_role_id'] = self.seller_ip_role_id.to_alipay_dict()
            else:
                params['seller_ip_role_id'] = self.seller_ip_role_id
        if self.seller_mid:
            if hasattr(self.seller_mid, 'to_alipay_dict'):
                params['seller_mid'] = self.seller_mid.to_alipay_dict()
            else:
                params['seller_mid'] = self.seller_mid
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.seller_telephone:
            if hasattr(self.seller_telephone, 'to_alipay_dict'):
                params['seller_telephone'] = self.seller_telephone.to_alipay_dict()
            else:
                params['seller_telephone'] = self.seller_telephone
        if self.tax_amt:
            if hasattr(self.tax_amt, 'to_alipay_dict'):
                params['tax_amt'] = self.tax_amt.to_alipay_dict()
            else:
                params['tax_amt'] = self.tax_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceAllResponseDTO()
        if 'attachment_name' in d:
            o.attachment_name = d['attachment_name']
        if 'attachment_oss_key' in d:
            o.attachment_oss_key = d['attachment_oss_key']
        if 'buyer_address' in d:
            o.buyer_address = d['buyer_address']
        if 'buyer_bank_account' in d:
            o.buyer_bank_account = d['buyer_bank_account']
        if 'buyer_bank_name' in d:
            o.buyer_bank_name = d['buyer_bank_name']
        if 'buyer_inst_id' in d:
            o.buyer_inst_id = d['buyer_inst_id']
        if 'buyer_invoice_title' in d:
            o.buyer_invoice_title = d['buyer_invoice_title']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'buyer_telephone' in d:
            o.buyer_telephone = d['buyer_telephone']
        if 'exclude_tax_amt' in d:
            o.exclude_tax_amt = d['exclude_tax_amt']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_auth_date' in d:
            o.invoice_auth_date = d['invoice_auth_date']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_line_list' in d:
            o.invoice_line_list = d['invoice_line_list']
        if 'invoice_mail_status' in d:
            o.invoice_mail_status = d['invoice_mail_status']
        if 'invoice_mail_status_name' in d:
            o.invoice_mail_status_name = d['invoice_mail_status_name']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'invoice_rcv_date' in d:
            o.invoice_rcv_date = d['invoice_rcv_date']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_status_name' in d:
            o.invoice_status_name = d['invoice_status_name']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'invoice_type_name' in d:
            o.invoice_type_name = d['invoice_type_name']
        if 'is_red' in d:
            o.is_red = d['is_red']
        if 'memo' in d:
            o.memo = d['memo']
        if 'relevant_amt' in d:
            o.relevant_amt = d['relevant_amt']
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_bank_account' in d:
            o.seller_bank_account = d['seller_bank_account']
        if 'seller_bank_name' in d:
            o.seller_bank_name = d['seller_bank_name']
        if 'seller_company_name' in d:
            o.seller_company_name = d['seller_company_name']
        if 'seller_custm_name' in d:
            o.seller_custm_name = d['seller_custm_name']
        if 'seller_ip_role_id' in d:
            o.seller_ip_role_id = d['seller_ip_role_id']
        if 'seller_mid' in d:
            o.seller_mid = d['seller_mid']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'seller_telephone' in d:
            o.seller_telephone = d['seller_telephone']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        return o


