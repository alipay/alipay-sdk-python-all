#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputInvoiceLineOpenApiDTO import InputInvoiceLineOpenApiDTO


class InputInvoiceOpenApiDTO(object):

    def __init__(self):
        self._amount = None
        self._authorized_dealer = None
        self._biz_type = None
        self._certify_status = None
        self._certify_status_memo = None
        self._certify_time = None
        self._certify_user = None
        self._check_status = None
        self._check_status_memo = None
        self._check_sum = None
        self._check_time = None
        self._cipher_text = None
        self._company_code = None
        self._currency = None
        self._discard_time = None
        self._distribute_status = None
        self._distribute_status_memo = None
        self._effective_tax_amount = None
        self._electronic_type = None
        self._excluding_tax_amount = None
        self._id = None
        self._image_file_name = None
        self._image_id = None
        self._image_url = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_issue_type = None
        self._invoice_line = None
        self._invoice_material = None
        self._invoice_material_memo = None
        self._invoice_no = None
        self._invoice_remark = None
        self._invoice_type = None
        self._invoice_type_memo = None
        self._issue_country_type = None
        self._issued_seller_name = None
        self._issued_tax_no = None
        self._machine_code = None
        self._purchaser_bank_info = None
        self._purchaser_code = None
        self._purchaser_contact_info = None
        self._purchaser_country_code = None
        self._purchaser_name = None
        self._purchaser_region_code = None
        self._purchaser_tax_no = None
        self._qr_code_cipher_text = None
        self._qr_code_flag = None
        self._reg_biz_identity_code = None
        self._reg_biz_identity_ou = None
        self._reg_platform_code = None
        self._reg_status = None
        self._reg_status_memo = None
        self._reg_time = None
        self._reg_user = None
        self._register_channel = None
        self._register_channel_memo = None
        self._related_order = None
        self._related_system = None
        self._return_time = None
        self._return_user = None
        self._return_waybill_company = None
        self._return_waybill_no = None
        self._scan_account = None
        self._seller_bank_info = None
        self._seller_code = None
        self._seller_contact_info = None
        self._seller_country_code = None
        self._seller_name = None
        self._seller_region_code = None
        self._seller_tax_no = None
        self._tax_amount = None
        self._tax_period = None
        self._tax_rate = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def authorized_dealer(self):
        return self._authorized_dealer

    @authorized_dealer.setter
    def authorized_dealer(self, value):
        self._authorized_dealer = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def certify_status(self):
        return self._certify_status

    @certify_status.setter
    def certify_status(self, value):
        self._certify_status = value
    @property
    def certify_status_memo(self):
        return self._certify_status_memo

    @certify_status_memo.setter
    def certify_status_memo(self, value):
        self._certify_status_memo = value
    @property
    def certify_time(self):
        return self._certify_time

    @certify_time.setter
    def certify_time(self, value):
        self._certify_time = value
    @property
    def certify_user(self):
        return self._certify_user

    @certify_user.setter
    def certify_user(self, value):
        self._certify_user = value
    @property
    def check_status(self):
        return self._check_status

    @check_status.setter
    def check_status(self, value):
        self._check_status = value
    @property
    def check_status_memo(self):
        return self._check_status_memo

    @check_status_memo.setter
    def check_status_memo(self, value):
        self._check_status_memo = value
    @property
    def check_sum(self):
        return self._check_sum

    @check_sum.setter
    def check_sum(self, value):
        self._check_sum = value
    @property
    def check_time(self):
        return self._check_time

    @check_time.setter
    def check_time(self, value):
        self._check_time = value
    @property
    def cipher_text(self):
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, value):
        self._cipher_text = value
    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def discard_time(self):
        return self._discard_time

    @discard_time.setter
    def discard_time(self, value):
        self._discard_time = value
    @property
    def distribute_status(self):
        return self._distribute_status

    @distribute_status.setter
    def distribute_status(self, value):
        self._distribute_status = value
    @property
    def distribute_status_memo(self):
        return self._distribute_status_memo

    @distribute_status_memo.setter
    def distribute_status_memo(self, value):
        self._distribute_status_memo = value
    @property
    def effective_tax_amount(self):
        return self._effective_tax_amount

    @effective_tax_amount.setter
    def effective_tax_amount(self, value):
        self._effective_tax_amount = value
    @property
    def electronic_type(self):
        return self._electronic_type

    @electronic_type.setter
    def electronic_type(self, value):
        self._electronic_type = value
    @property
    def excluding_tax_amount(self):
        return self._excluding_tax_amount

    @excluding_tax_amount.setter
    def excluding_tax_amount(self, value):
        self._excluding_tax_amount = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def image_file_name(self):
        return self._image_file_name

    @image_file_name.setter
    def image_file_name(self, value):
        self._image_file_name = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
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
    def invoice_issue_type(self):
        return self._invoice_issue_type

    @invoice_issue_type.setter
    def invoice_issue_type(self, value):
        self._invoice_issue_type = value
    @property
    def invoice_line(self):
        return self._invoice_line

    @invoice_line.setter
    def invoice_line(self, value):
        if isinstance(value, list):
            self._invoice_line = list()
            for i in value:
                if isinstance(i, InputInvoiceLineOpenApiDTO):
                    self._invoice_line.append(i)
                else:
                    self._invoice_line.append(InputInvoiceLineOpenApiDTO.from_alipay_dict(i))
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
    @property
    def invoice_material_memo(self):
        return self._invoice_material_memo

    @invoice_material_memo.setter
    def invoice_material_memo(self, value):
        self._invoice_material_memo = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_remark(self):
        return self._invoice_remark

    @invoice_remark.setter
    def invoice_remark(self, value):
        self._invoice_remark = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def invoice_type_memo(self):
        return self._invoice_type_memo

    @invoice_type_memo.setter
    def invoice_type_memo(self, value):
        self._invoice_type_memo = value
    @property
    def issue_country_type(self):
        return self._issue_country_type

    @issue_country_type.setter
    def issue_country_type(self, value):
        self._issue_country_type = value
    @property
    def issued_seller_name(self):
        return self._issued_seller_name

    @issued_seller_name.setter
    def issued_seller_name(self, value):
        self._issued_seller_name = value
    @property
    def issued_tax_no(self):
        return self._issued_tax_no

    @issued_tax_no.setter
    def issued_tax_no(self, value):
        self._issued_tax_no = value
    @property
    def machine_code(self):
        return self._machine_code

    @machine_code.setter
    def machine_code(self, value):
        self._machine_code = value
    @property
    def purchaser_bank_info(self):
        return self._purchaser_bank_info

    @purchaser_bank_info.setter
    def purchaser_bank_info(self, value):
        self._purchaser_bank_info = value
    @property
    def purchaser_code(self):
        return self._purchaser_code

    @purchaser_code.setter
    def purchaser_code(self, value):
        self._purchaser_code = value
    @property
    def purchaser_contact_info(self):
        return self._purchaser_contact_info

    @purchaser_contact_info.setter
    def purchaser_contact_info(self, value):
        self._purchaser_contact_info = value
    @property
    def purchaser_country_code(self):
        return self._purchaser_country_code

    @purchaser_country_code.setter
    def purchaser_country_code(self, value):
        self._purchaser_country_code = value
    @property
    def purchaser_name(self):
        return self._purchaser_name

    @purchaser_name.setter
    def purchaser_name(self, value):
        self._purchaser_name = value
    @property
    def purchaser_region_code(self):
        return self._purchaser_region_code

    @purchaser_region_code.setter
    def purchaser_region_code(self, value):
        self._purchaser_region_code = value
    @property
    def purchaser_tax_no(self):
        return self._purchaser_tax_no

    @purchaser_tax_no.setter
    def purchaser_tax_no(self, value):
        self._purchaser_tax_no = value
    @property
    def qr_code_cipher_text(self):
        return self._qr_code_cipher_text

    @qr_code_cipher_text.setter
    def qr_code_cipher_text(self, value):
        self._qr_code_cipher_text = value
    @property
    def qr_code_flag(self):
        return self._qr_code_flag

    @qr_code_flag.setter
    def qr_code_flag(self, value):
        self._qr_code_flag = value
    @property
    def reg_biz_identity_code(self):
        return self._reg_biz_identity_code

    @reg_biz_identity_code.setter
    def reg_biz_identity_code(self, value):
        self._reg_biz_identity_code = value
    @property
    def reg_biz_identity_ou(self):
        return self._reg_biz_identity_ou

    @reg_biz_identity_ou.setter
    def reg_biz_identity_ou(self, value):
        self._reg_biz_identity_ou = value
    @property
    def reg_platform_code(self):
        return self._reg_platform_code

    @reg_platform_code.setter
    def reg_platform_code(self, value):
        self._reg_platform_code = value
    @property
    def reg_status(self):
        return self._reg_status

    @reg_status.setter
    def reg_status(self, value):
        self._reg_status = value
    @property
    def reg_status_memo(self):
        return self._reg_status_memo

    @reg_status_memo.setter
    def reg_status_memo(self, value):
        self._reg_status_memo = value
    @property
    def reg_time(self):
        return self._reg_time

    @reg_time.setter
    def reg_time(self, value):
        self._reg_time = value
    @property
    def reg_user(self):
        return self._reg_user

    @reg_user.setter
    def reg_user(self, value):
        self._reg_user = value
    @property
    def register_channel(self):
        return self._register_channel

    @register_channel.setter
    def register_channel(self, value):
        self._register_channel = value
    @property
    def register_channel_memo(self):
        return self._register_channel_memo

    @register_channel_memo.setter
    def register_channel_memo(self, value):
        self._register_channel_memo = value
    @property
    def related_order(self):
        return self._related_order

    @related_order.setter
    def related_order(self, value):
        self._related_order = value
    @property
    def related_system(self):
        return self._related_system

    @related_system.setter
    def related_system(self, value):
        self._related_system = value
    @property
    def return_time(self):
        return self._return_time

    @return_time.setter
    def return_time(self, value):
        self._return_time = value
    @property
    def return_user(self):
        return self._return_user

    @return_user.setter
    def return_user(self, value):
        self._return_user = value
    @property
    def return_waybill_company(self):
        return self._return_waybill_company

    @return_waybill_company.setter
    def return_waybill_company(self, value):
        self._return_waybill_company = value
    @property
    def return_waybill_no(self):
        return self._return_waybill_no

    @return_waybill_no.setter
    def return_waybill_no(self, value):
        self._return_waybill_no = value
    @property
    def scan_account(self):
        return self._scan_account

    @scan_account.setter
    def scan_account(self, value):
        self._scan_account = value
    @property
    def seller_bank_info(self):
        return self._seller_bank_info

    @seller_bank_info.setter
    def seller_bank_info(self, value):
        self._seller_bank_info = value
    @property
    def seller_code(self):
        return self._seller_code

    @seller_code.setter
    def seller_code(self, value):
        self._seller_code = value
    @property
    def seller_contact_info(self):
        return self._seller_contact_info

    @seller_contact_info.setter
    def seller_contact_info(self, value):
        self._seller_contact_info = value
    @property
    def seller_country_code(self):
        return self._seller_country_code

    @seller_country_code.setter
    def seller_country_code(self, value):
        self._seller_country_code = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def seller_region_code(self):
        return self._seller_region_code

    @seller_region_code.setter
    def seller_region_code(self, value):
        self._seller_region_code = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_period(self):
        return self._tax_period

    @tax_period.setter
    def tax_period(self, value):
        self._tax_period = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.authorized_dealer:
            if hasattr(self.authorized_dealer, 'to_alipay_dict'):
                params['authorized_dealer'] = self.authorized_dealer.to_alipay_dict()
            else:
                params['authorized_dealer'] = self.authorized_dealer
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.certify_status:
            if hasattr(self.certify_status, 'to_alipay_dict'):
                params['certify_status'] = self.certify_status.to_alipay_dict()
            else:
                params['certify_status'] = self.certify_status
        if self.certify_status_memo:
            if hasattr(self.certify_status_memo, 'to_alipay_dict'):
                params['certify_status_memo'] = self.certify_status_memo.to_alipay_dict()
            else:
                params['certify_status_memo'] = self.certify_status_memo
        if self.certify_time:
            if hasattr(self.certify_time, 'to_alipay_dict'):
                params['certify_time'] = self.certify_time.to_alipay_dict()
            else:
                params['certify_time'] = self.certify_time
        if self.certify_user:
            if hasattr(self.certify_user, 'to_alipay_dict'):
                params['certify_user'] = self.certify_user.to_alipay_dict()
            else:
                params['certify_user'] = self.certify_user
        if self.check_status:
            if hasattr(self.check_status, 'to_alipay_dict'):
                params['check_status'] = self.check_status.to_alipay_dict()
            else:
                params['check_status'] = self.check_status
        if self.check_status_memo:
            if hasattr(self.check_status_memo, 'to_alipay_dict'):
                params['check_status_memo'] = self.check_status_memo.to_alipay_dict()
            else:
                params['check_status_memo'] = self.check_status_memo
        if self.check_sum:
            if hasattr(self.check_sum, 'to_alipay_dict'):
                params['check_sum'] = self.check_sum.to_alipay_dict()
            else:
                params['check_sum'] = self.check_sum
        if self.check_time:
            if hasattr(self.check_time, 'to_alipay_dict'):
                params['check_time'] = self.check_time.to_alipay_dict()
            else:
                params['check_time'] = self.check_time
        if self.cipher_text:
            if hasattr(self.cipher_text, 'to_alipay_dict'):
                params['cipher_text'] = self.cipher_text.to_alipay_dict()
            else:
                params['cipher_text'] = self.cipher_text
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.discard_time:
            if hasattr(self.discard_time, 'to_alipay_dict'):
                params['discard_time'] = self.discard_time.to_alipay_dict()
            else:
                params['discard_time'] = self.discard_time
        if self.distribute_status:
            if hasattr(self.distribute_status, 'to_alipay_dict'):
                params['distribute_status'] = self.distribute_status.to_alipay_dict()
            else:
                params['distribute_status'] = self.distribute_status
        if self.distribute_status_memo:
            if hasattr(self.distribute_status_memo, 'to_alipay_dict'):
                params['distribute_status_memo'] = self.distribute_status_memo.to_alipay_dict()
            else:
                params['distribute_status_memo'] = self.distribute_status_memo
        if self.effective_tax_amount:
            if hasattr(self.effective_tax_amount, 'to_alipay_dict'):
                params['effective_tax_amount'] = self.effective_tax_amount.to_alipay_dict()
            else:
                params['effective_tax_amount'] = self.effective_tax_amount
        if self.electronic_type:
            if hasattr(self.electronic_type, 'to_alipay_dict'):
                params['electronic_type'] = self.electronic_type.to_alipay_dict()
            else:
                params['electronic_type'] = self.electronic_type
        if self.excluding_tax_amount:
            if hasattr(self.excluding_tax_amount, 'to_alipay_dict'):
                params['excluding_tax_amount'] = self.excluding_tax_amount.to_alipay_dict()
            else:
                params['excluding_tax_amount'] = self.excluding_tax_amount
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.image_file_name:
            if hasattr(self.image_file_name, 'to_alipay_dict'):
                params['image_file_name'] = self.image_file_name.to_alipay_dict()
            else:
                params['image_file_name'] = self.image_file_name
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
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
        if self.invoice_issue_type:
            if hasattr(self.invoice_issue_type, 'to_alipay_dict'):
                params['invoice_issue_type'] = self.invoice_issue_type.to_alipay_dict()
            else:
                params['invoice_issue_type'] = self.invoice_issue_type
        if self.invoice_line:
            if isinstance(self.invoice_line, list):
                for i in range(0, len(self.invoice_line)):
                    element = self.invoice_line[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_line[i] = element.to_alipay_dict()
            if hasattr(self.invoice_line, 'to_alipay_dict'):
                params['invoice_line'] = self.invoice_line.to_alipay_dict()
            else:
                params['invoice_line'] = self.invoice_line
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
        if self.invoice_material_memo:
            if hasattr(self.invoice_material_memo, 'to_alipay_dict'):
                params['invoice_material_memo'] = self.invoice_material_memo.to_alipay_dict()
            else:
                params['invoice_material_memo'] = self.invoice_material_memo
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_remark:
            if hasattr(self.invoice_remark, 'to_alipay_dict'):
                params['invoice_remark'] = self.invoice_remark.to_alipay_dict()
            else:
                params['invoice_remark'] = self.invoice_remark
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.invoice_type_memo:
            if hasattr(self.invoice_type_memo, 'to_alipay_dict'):
                params['invoice_type_memo'] = self.invoice_type_memo.to_alipay_dict()
            else:
                params['invoice_type_memo'] = self.invoice_type_memo
        if self.issue_country_type:
            if hasattr(self.issue_country_type, 'to_alipay_dict'):
                params['issue_country_type'] = self.issue_country_type.to_alipay_dict()
            else:
                params['issue_country_type'] = self.issue_country_type
        if self.issued_seller_name:
            if hasattr(self.issued_seller_name, 'to_alipay_dict'):
                params['issued_seller_name'] = self.issued_seller_name.to_alipay_dict()
            else:
                params['issued_seller_name'] = self.issued_seller_name
        if self.issued_tax_no:
            if hasattr(self.issued_tax_no, 'to_alipay_dict'):
                params['issued_tax_no'] = self.issued_tax_no.to_alipay_dict()
            else:
                params['issued_tax_no'] = self.issued_tax_no
        if self.machine_code:
            if hasattr(self.machine_code, 'to_alipay_dict'):
                params['machine_code'] = self.machine_code.to_alipay_dict()
            else:
                params['machine_code'] = self.machine_code
        if self.purchaser_bank_info:
            if hasattr(self.purchaser_bank_info, 'to_alipay_dict'):
                params['purchaser_bank_info'] = self.purchaser_bank_info.to_alipay_dict()
            else:
                params['purchaser_bank_info'] = self.purchaser_bank_info
        if self.purchaser_code:
            if hasattr(self.purchaser_code, 'to_alipay_dict'):
                params['purchaser_code'] = self.purchaser_code.to_alipay_dict()
            else:
                params['purchaser_code'] = self.purchaser_code
        if self.purchaser_contact_info:
            if hasattr(self.purchaser_contact_info, 'to_alipay_dict'):
                params['purchaser_contact_info'] = self.purchaser_contact_info.to_alipay_dict()
            else:
                params['purchaser_contact_info'] = self.purchaser_contact_info
        if self.purchaser_country_code:
            if hasattr(self.purchaser_country_code, 'to_alipay_dict'):
                params['purchaser_country_code'] = self.purchaser_country_code.to_alipay_dict()
            else:
                params['purchaser_country_code'] = self.purchaser_country_code
        if self.purchaser_name:
            if hasattr(self.purchaser_name, 'to_alipay_dict'):
                params['purchaser_name'] = self.purchaser_name.to_alipay_dict()
            else:
                params['purchaser_name'] = self.purchaser_name
        if self.purchaser_region_code:
            if hasattr(self.purchaser_region_code, 'to_alipay_dict'):
                params['purchaser_region_code'] = self.purchaser_region_code.to_alipay_dict()
            else:
                params['purchaser_region_code'] = self.purchaser_region_code
        if self.purchaser_tax_no:
            if hasattr(self.purchaser_tax_no, 'to_alipay_dict'):
                params['purchaser_tax_no'] = self.purchaser_tax_no.to_alipay_dict()
            else:
                params['purchaser_tax_no'] = self.purchaser_tax_no
        if self.qr_code_cipher_text:
            if hasattr(self.qr_code_cipher_text, 'to_alipay_dict'):
                params['qr_code_cipher_text'] = self.qr_code_cipher_text.to_alipay_dict()
            else:
                params['qr_code_cipher_text'] = self.qr_code_cipher_text
        if self.qr_code_flag:
            if hasattr(self.qr_code_flag, 'to_alipay_dict'):
                params['qr_code_flag'] = self.qr_code_flag.to_alipay_dict()
            else:
                params['qr_code_flag'] = self.qr_code_flag
        if self.reg_biz_identity_code:
            if hasattr(self.reg_biz_identity_code, 'to_alipay_dict'):
                params['reg_biz_identity_code'] = self.reg_biz_identity_code.to_alipay_dict()
            else:
                params['reg_biz_identity_code'] = self.reg_biz_identity_code
        if self.reg_biz_identity_ou:
            if hasattr(self.reg_biz_identity_ou, 'to_alipay_dict'):
                params['reg_biz_identity_ou'] = self.reg_biz_identity_ou.to_alipay_dict()
            else:
                params['reg_biz_identity_ou'] = self.reg_biz_identity_ou
        if self.reg_platform_code:
            if hasattr(self.reg_platform_code, 'to_alipay_dict'):
                params['reg_platform_code'] = self.reg_platform_code.to_alipay_dict()
            else:
                params['reg_platform_code'] = self.reg_platform_code
        if self.reg_status:
            if hasattr(self.reg_status, 'to_alipay_dict'):
                params['reg_status'] = self.reg_status.to_alipay_dict()
            else:
                params['reg_status'] = self.reg_status
        if self.reg_status_memo:
            if hasattr(self.reg_status_memo, 'to_alipay_dict'):
                params['reg_status_memo'] = self.reg_status_memo.to_alipay_dict()
            else:
                params['reg_status_memo'] = self.reg_status_memo
        if self.reg_time:
            if hasattr(self.reg_time, 'to_alipay_dict'):
                params['reg_time'] = self.reg_time.to_alipay_dict()
            else:
                params['reg_time'] = self.reg_time
        if self.reg_user:
            if hasattr(self.reg_user, 'to_alipay_dict'):
                params['reg_user'] = self.reg_user.to_alipay_dict()
            else:
                params['reg_user'] = self.reg_user
        if self.register_channel:
            if hasattr(self.register_channel, 'to_alipay_dict'):
                params['register_channel'] = self.register_channel.to_alipay_dict()
            else:
                params['register_channel'] = self.register_channel
        if self.register_channel_memo:
            if hasattr(self.register_channel_memo, 'to_alipay_dict'):
                params['register_channel_memo'] = self.register_channel_memo.to_alipay_dict()
            else:
                params['register_channel_memo'] = self.register_channel_memo
        if self.related_order:
            if hasattr(self.related_order, 'to_alipay_dict'):
                params['related_order'] = self.related_order.to_alipay_dict()
            else:
                params['related_order'] = self.related_order
        if self.related_system:
            if hasattr(self.related_system, 'to_alipay_dict'):
                params['related_system'] = self.related_system.to_alipay_dict()
            else:
                params['related_system'] = self.related_system
        if self.return_time:
            if hasattr(self.return_time, 'to_alipay_dict'):
                params['return_time'] = self.return_time.to_alipay_dict()
            else:
                params['return_time'] = self.return_time
        if self.return_user:
            if hasattr(self.return_user, 'to_alipay_dict'):
                params['return_user'] = self.return_user.to_alipay_dict()
            else:
                params['return_user'] = self.return_user
        if self.return_waybill_company:
            if hasattr(self.return_waybill_company, 'to_alipay_dict'):
                params['return_waybill_company'] = self.return_waybill_company.to_alipay_dict()
            else:
                params['return_waybill_company'] = self.return_waybill_company
        if self.return_waybill_no:
            if hasattr(self.return_waybill_no, 'to_alipay_dict'):
                params['return_waybill_no'] = self.return_waybill_no.to_alipay_dict()
            else:
                params['return_waybill_no'] = self.return_waybill_no
        if self.scan_account:
            if hasattr(self.scan_account, 'to_alipay_dict'):
                params['scan_account'] = self.scan_account.to_alipay_dict()
            else:
                params['scan_account'] = self.scan_account
        if self.seller_bank_info:
            if hasattr(self.seller_bank_info, 'to_alipay_dict'):
                params['seller_bank_info'] = self.seller_bank_info.to_alipay_dict()
            else:
                params['seller_bank_info'] = self.seller_bank_info
        if self.seller_code:
            if hasattr(self.seller_code, 'to_alipay_dict'):
                params['seller_code'] = self.seller_code.to_alipay_dict()
            else:
                params['seller_code'] = self.seller_code
        if self.seller_contact_info:
            if hasattr(self.seller_contact_info, 'to_alipay_dict'):
                params['seller_contact_info'] = self.seller_contact_info.to_alipay_dict()
            else:
                params['seller_contact_info'] = self.seller_contact_info
        if self.seller_country_code:
            if hasattr(self.seller_country_code, 'to_alipay_dict'):
                params['seller_country_code'] = self.seller_country_code.to_alipay_dict()
            else:
                params['seller_country_code'] = self.seller_country_code
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.seller_region_code:
            if hasattr(self.seller_region_code, 'to_alipay_dict'):
                params['seller_region_code'] = self.seller_region_code.to_alipay_dict()
            else:
                params['seller_region_code'] = self.seller_region_code
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_period:
            if hasattr(self.tax_period, 'to_alipay_dict'):
                params['tax_period'] = self.tax_period.to_alipay_dict()
            else:
                params['tax_period'] = self.tax_period
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceOpenApiDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'authorized_dealer' in d:
            o.authorized_dealer = d['authorized_dealer']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'certify_status' in d:
            o.certify_status = d['certify_status']
        if 'certify_status_memo' in d:
            o.certify_status_memo = d['certify_status_memo']
        if 'certify_time' in d:
            o.certify_time = d['certify_time']
        if 'certify_user' in d:
            o.certify_user = d['certify_user']
        if 'check_status' in d:
            o.check_status = d['check_status']
        if 'check_status_memo' in d:
            o.check_status_memo = d['check_status_memo']
        if 'check_sum' in d:
            o.check_sum = d['check_sum']
        if 'check_time' in d:
            o.check_time = d['check_time']
        if 'cipher_text' in d:
            o.cipher_text = d['cipher_text']
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'discard_time' in d:
            o.discard_time = d['discard_time']
        if 'distribute_status' in d:
            o.distribute_status = d['distribute_status']
        if 'distribute_status_memo' in d:
            o.distribute_status_memo = d['distribute_status_memo']
        if 'effective_tax_amount' in d:
            o.effective_tax_amount = d['effective_tax_amount']
        if 'electronic_type' in d:
            o.electronic_type = d['electronic_type']
        if 'excluding_tax_amount' in d:
            o.excluding_tax_amount = d['excluding_tax_amount']
        if 'id' in d:
            o.id = d['id']
        if 'image_file_name' in d:
            o.image_file_name = d['image_file_name']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_issue_type' in d:
            o.invoice_issue_type = d['invoice_issue_type']
        if 'invoice_line' in d:
            o.invoice_line = d['invoice_line']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_material_memo' in d:
            o.invoice_material_memo = d['invoice_material_memo']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_remark' in d:
            o.invoice_remark = d['invoice_remark']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'invoice_type_memo' in d:
            o.invoice_type_memo = d['invoice_type_memo']
        if 'issue_country_type' in d:
            o.issue_country_type = d['issue_country_type']
        if 'issued_seller_name' in d:
            o.issued_seller_name = d['issued_seller_name']
        if 'issued_tax_no' in d:
            o.issued_tax_no = d['issued_tax_no']
        if 'machine_code' in d:
            o.machine_code = d['machine_code']
        if 'purchaser_bank_info' in d:
            o.purchaser_bank_info = d['purchaser_bank_info']
        if 'purchaser_code' in d:
            o.purchaser_code = d['purchaser_code']
        if 'purchaser_contact_info' in d:
            o.purchaser_contact_info = d['purchaser_contact_info']
        if 'purchaser_country_code' in d:
            o.purchaser_country_code = d['purchaser_country_code']
        if 'purchaser_name' in d:
            o.purchaser_name = d['purchaser_name']
        if 'purchaser_region_code' in d:
            o.purchaser_region_code = d['purchaser_region_code']
        if 'purchaser_tax_no' in d:
            o.purchaser_tax_no = d['purchaser_tax_no']
        if 'qr_code_cipher_text' in d:
            o.qr_code_cipher_text = d['qr_code_cipher_text']
        if 'qr_code_flag' in d:
            o.qr_code_flag = d['qr_code_flag']
        if 'reg_biz_identity_code' in d:
            o.reg_biz_identity_code = d['reg_biz_identity_code']
        if 'reg_biz_identity_ou' in d:
            o.reg_biz_identity_ou = d['reg_biz_identity_ou']
        if 'reg_platform_code' in d:
            o.reg_platform_code = d['reg_platform_code']
        if 'reg_status' in d:
            o.reg_status = d['reg_status']
        if 'reg_status_memo' in d:
            o.reg_status_memo = d['reg_status_memo']
        if 'reg_time' in d:
            o.reg_time = d['reg_time']
        if 'reg_user' in d:
            o.reg_user = d['reg_user']
        if 'register_channel' in d:
            o.register_channel = d['register_channel']
        if 'register_channel_memo' in d:
            o.register_channel_memo = d['register_channel_memo']
        if 'related_order' in d:
            o.related_order = d['related_order']
        if 'related_system' in d:
            o.related_system = d['related_system']
        if 'return_time' in d:
            o.return_time = d['return_time']
        if 'return_user' in d:
            o.return_user = d['return_user']
        if 'return_waybill_company' in d:
            o.return_waybill_company = d['return_waybill_company']
        if 'return_waybill_no' in d:
            o.return_waybill_no = d['return_waybill_no']
        if 'scan_account' in d:
            o.scan_account = d['scan_account']
        if 'seller_bank_info' in d:
            o.seller_bank_info = d['seller_bank_info']
        if 'seller_code' in d:
            o.seller_code = d['seller_code']
        if 'seller_contact_info' in d:
            o.seller_contact_info = d['seller_contact_info']
        if 'seller_country_code' in d:
            o.seller_country_code = d['seller_country_code']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'seller_region_code' in d:
            o.seller_region_code = d['seller_region_code']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_period' in d:
            o.tax_period = d['tax_period']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


