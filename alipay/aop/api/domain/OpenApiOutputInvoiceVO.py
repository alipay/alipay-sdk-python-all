#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.OpenApiInvoiceLineVO import OpenApiInvoiceLineVO
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class OpenApiOutputInvoiceVO(object):

    def __init__(self):
        self._attachment_name = None
        self._attachment_oss_key = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_invoice_title = None
        self._buyer_ip_role_id = None
        self._buyer_mid = None
        self._buyer_tax_no = None
        self._buyer_telephone = None
        self._can_link = None
        self._creator = None
        self._drawer = None
        self._elc_invoice_url = None
        self._gmt_auth = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_relevant = None
        self._invoice_amt = None
        self._invoice_channel = None
        self._invoice_code = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_lines = None
        self._invoice_material = None
        self._invoice_no = None
        self._invoice_note = None
        self._invoice_status = None
        self._invoice_type = None
        self._is_online = None
        self._is_red = None
        self._last_moder = None
        self._linked_amt = None
        self._mail_status = None
        self._memo = None
        self._no_bill_invoice_flag = None
        self._payee = None
        self._proforma_invoice_html = None
        self._recent_mail_id = None
        self._red_amt = None
        self._red_notice_no = None
        self._reviewer = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_company_name = None
        self._seller_inst_id = None
        self._seller_tax_no = None
        self._seller_telephone = None
        self._tax_amt = None
        self._template_url = None
        self._tnt_inst_id = None

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
    def buyer_invoice_title(self):
        return self._buyer_invoice_title

    @buyer_invoice_title.setter
    def buyer_invoice_title(self, value):
        self._buyer_invoice_title = value
    @property
    def buyer_ip_role_id(self):
        return self._buyer_ip_role_id

    @buyer_ip_role_id.setter
    def buyer_ip_role_id(self, value):
        self._buyer_ip_role_id = value
    @property
    def buyer_mid(self):
        return self._buyer_mid

    @buyer_mid.setter
    def buyer_mid(self, value):
        self._buyer_mid = value
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
    def can_link(self):
        return self._can_link

    @can_link.setter
    def can_link(self, value):
        self._can_link = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def drawer(self):
        return self._drawer

    @drawer.setter
    def drawer(self, value):
        self._drawer = value
    @property
    def elc_invoice_url(self):
        return self._elc_invoice_url

    @elc_invoice_url.setter
    def elc_invoice_url(self, value):
        self._elc_invoice_url = value
    @property
    def gmt_auth(self):
        return self._gmt_auth

    @gmt_auth.setter
    def gmt_auth(self, value):
        self._gmt_auth = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_relevant(self):
        return self._gmt_relevant

    @gmt_relevant.setter
    def gmt_relevant(self, value):
        self._gmt_relevant = value
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
    def invoice_channel(self):
        return self._invoice_channel

    @invoice_channel.setter
    def invoice_channel(self, value):
        self._invoice_channel = value
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
    def invoice_lines(self):
        return self._invoice_lines

    @invoice_lines.setter
    def invoice_lines(self, value):
        if isinstance(value, list):
            self._invoice_lines = list()
            for i in value:
                if isinstance(i, OpenApiInvoiceLineVO):
                    self._invoice_lines.append(i)
                else:
                    self._invoice_lines.append(OpenApiInvoiceLineVO.from_alipay_dict(i))
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
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
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def is_red(self):
        return self._is_red

    @is_red.setter
    def is_red(self, value):
        self._is_red = value
    @property
    def last_moder(self):
        return self._last_moder

    @last_moder.setter
    def last_moder(self, value):
        self._last_moder = value
    @property
    def linked_amt(self):
        return self._linked_amt

    @linked_amt.setter
    def linked_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._linked_amt = value
        else:
            self._linked_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def mail_status(self):
        return self._mail_status

    @mail_status.setter
    def mail_status(self, value):
        self._mail_status = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def no_bill_invoice_flag(self):
        return self._no_bill_invoice_flag

    @no_bill_invoice_flag.setter
    def no_bill_invoice_flag(self, value):
        self._no_bill_invoice_flag = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def proforma_invoice_html(self):
        return self._proforma_invoice_html

    @proforma_invoice_html.setter
    def proforma_invoice_html(self, value):
        self._proforma_invoice_html = value
    @property
    def recent_mail_id(self):
        return self._recent_mail_id

    @recent_mail_id.setter
    def recent_mail_id(self, value):
        self._recent_mail_id = value
    @property
    def red_amt(self):
        return self._red_amt

    @red_amt.setter
    def red_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._red_amt = value
        else:
            self._red_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def red_notice_no(self):
        return self._red_notice_no

    @red_notice_no.setter
    def red_notice_no(self, value):
        self._red_notice_no = value
    @property
    def reviewer(self):
        return self._reviewer

    @reviewer.setter
    def reviewer(self, value):
        self._reviewer = value
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
    def seller_inst_id(self):
        return self._seller_inst_id

    @seller_inst_id.setter
    def seller_inst_id(self, value):
        self._seller_inst_id = value
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
    @property
    def template_url(self):
        return self._template_url

    @template_url.setter
    def template_url(self, value):
        self._template_url = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


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
        if self.buyer_invoice_title:
            if hasattr(self.buyer_invoice_title, 'to_alipay_dict'):
                params['buyer_invoice_title'] = self.buyer_invoice_title.to_alipay_dict()
            else:
                params['buyer_invoice_title'] = self.buyer_invoice_title
        if self.buyer_ip_role_id:
            if hasattr(self.buyer_ip_role_id, 'to_alipay_dict'):
                params['buyer_ip_role_id'] = self.buyer_ip_role_id.to_alipay_dict()
            else:
                params['buyer_ip_role_id'] = self.buyer_ip_role_id
        if self.buyer_mid:
            if hasattr(self.buyer_mid, 'to_alipay_dict'):
                params['buyer_mid'] = self.buyer_mid.to_alipay_dict()
            else:
                params['buyer_mid'] = self.buyer_mid
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
        if self.can_link:
            if hasattr(self.can_link, 'to_alipay_dict'):
                params['can_link'] = self.can_link.to_alipay_dict()
            else:
                params['can_link'] = self.can_link
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.drawer:
            if hasattr(self.drawer, 'to_alipay_dict'):
                params['drawer'] = self.drawer.to_alipay_dict()
            else:
                params['drawer'] = self.drawer
        if self.elc_invoice_url:
            if hasattr(self.elc_invoice_url, 'to_alipay_dict'):
                params['elc_invoice_url'] = self.elc_invoice_url.to_alipay_dict()
            else:
                params['elc_invoice_url'] = self.elc_invoice_url
        if self.gmt_auth:
            if hasattr(self.gmt_auth, 'to_alipay_dict'):
                params['gmt_auth'] = self.gmt_auth.to_alipay_dict()
            else:
                params['gmt_auth'] = self.gmt_auth
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.gmt_relevant:
            if hasattr(self.gmt_relevant, 'to_alipay_dict'):
                params['gmt_relevant'] = self.gmt_relevant.to_alipay_dict()
            else:
                params['gmt_relevant'] = self.gmt_relevant
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_channel:
            if hasattr(self.invoice_channel, 'to_alipay_dict'):
                params['invoice_channel'] = self.invoice_channel.to_alipay_dict()
            else:
                params['invoice_channel'] = self.invoice_channel
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
        if self.invoice_lines:
            if isinstance(self.invoice_lines, list):
                for i in range(0, len(self.invoice_lines)):
                    element = self.invoice_lines[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_lines[i] = element.to_alipay_dict()
            if hasattr(self.invoice_lines, 'to_alipay_dict'):
                params['invoice_lines'] = self.invoice_lines.to_alipay_dict()
            else:
                params['invoice_lines'] = self.invoice_lines
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
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
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.is_online:
            if hasattr(self.is_online, 'to_alipay_dict'):
                params['is_online'] = self.is_online.to_alipay_dict()
            else:
                params['is_online'] = self.is_online
        if self.is_red:
            if hasattr(self.is_red, 'to_alipay_dict'):
                params['is_red'] = self.is_red.to_alipay_dict()
            else:
                params['is_red'] = self.is_red
        if self.last_moder:
            if hasattr(self.last_moder, 'to_alipay_dict'):
                params['last_moder'] = self.last_moder.to_alipay_dict()
            else:
                params['last_moder'] = self.last_moder
        if self.linked_amt:
            if hasattr(self.linked_amt, 'to_alipay_dict'):
                params['linked_amt'] = self.linked_amt.to_alipay_dict()
            else:
                params['linked_amt'] = self.linked_amt
        if self.mail_status:
            if hasattr(self.mail_status, 'to_alipay_dict'):
                params['mail_status'] = self.mail_status.to_alipay_dict()
            else:
                params['mail_status'] = self.mail_status
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.no_bill_invoice_flag:
            if hasattr(self.no_bill_invoice_flag, 'to_alipay_dict'):
                params['no_bill_invoice_flag'] = self.no_bill_invoice_flag.to_alipay_dict()
            else:
                params['no_bill_invoice_flag'] = self.no_bill_invoice_flag
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.proforma_invoice_html:
            if hasattr(self.proforma_invoice_html, 'to_alipay_dict'):
                params['proforma_invoice_html'] = self.proforma_invoice_html.to_alipay_dict()
            else:
                params['proforma_invoice_html'] = self.proforma_invoice_html
        if self.recent_mail_id:
            if hasattr(self.recent_mail_id, 'to_alipay_dict'):
                params['recent_mail_id'] = self.recent_mail_id.to_alipay_dict()
            else:
                params['recent_mail_id'] = self.recent_mail_id
        if self.red_amt:
            if hasattr(self.red_amt, 'to_alipay_dict'):
                params['red_amt'] = self.red_amt.to_alipay_dict()
            else:
                params['red_amt'] = self.red_amt
        if self.red_notice_no:
            if hasattr(self.red_notice_no, 'to_alipay_dict'):
                params['red_notice_no'] = self.red_notice_no.to_alipay_dict()
            else:
                params['red_notice_no'] = self.red_notice_no
        if self.reviewer:
            if hasattr(self.reviewer, 'to_alipay_dict'):
                params['reviewer'] = self.reviewer.to_alipay_dict()
            else:
                params['reviewer'] = self.reviewer
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
        if self.seller_inst_id:
            if hasattr(self.seller_inst_id, 'to_alipay_dict'):
                params['seller_inst_id'] = self.seller_inst_id.to_alipay_dict()
            else:
                params['seller_inst_id'] = self.seller_inst_id
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
        if self.template_url:
            if hasattr(self.template_url, 'to_alipay_dict'):
                params['template_url'] = self.template_url.to_alipay_dict()
            else:
                params['template_url'] = self.template_url
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOutputInvoiceVO()
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
        if 'buyer_invoice_title' in d:
            o.buyer_invoice_title = d['buyer_invoice_title']
        if 'buyer_ip_role_id' in d:
            o.buyer_ip_role_id = d['buyer_ip_role_id']
        if 'buyer_mid' in d:
            o.buyer_mid = d['buyer_mid']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'buyer_telephone' in d:
            o.buyer_telephone = d['buyer_telephone']
        if 'can_link' in d:
            o.can_link = d['can_link']
        if 'creator' in d:
            o.creator = d['creator']
        if 'drawer' in d:
            o.drawer = d['drawer']
        if 'elc_invoice_url' in d:
            o.elc_invoice_url = d['elc_invoice_url']
        if 'gmt_auth' in d:
            o.gmt_auth = d['gmt_auth']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gmt_relevant' in d:
            o.gmt_relevant = d['gmt_relevant']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_channel' in d:
            o.invoice_channel = d['invoice_channel']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_lines' in d:
            o.invoice_lines = d['invoice_lines']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'is_online' in d:
            o.is_online = d['is_online']
        if 'is_red' in d:
            o.is_red = d['is_red']
        if 'last_moder' in d:
            o.last_moder = d['last_moder']
        if 'linked_amt' in d:
            o.linked_amt = d['linked_amt']
        if 'mail_status' in d:
            o.mail_status = d['mail_status']
        if 'memo' in d:
            o.memo = d['memo']
        if 'no_bill_invoice_flag' in d:
            o.no_bill_invoice_flag = d['no_bill_invoice_flag']
        if 'payee' in d:
            o.payee = d['payee']
        if 'proforma_invoice_html' in d:
            o.proforma_invoice_html = d['proforma_invoice_html']
        if 'recent_mail_id' in d:
            o.recent_mail_id = d['recent_mail_id']
        if 'red_amt' in d:
            o.red_amt = d['red_amt']
        if 'red_notice_no' in d:
            o.red_notice_no = d['red_notice_no']
        if 'reviewer' in d:
            o.reviewer = d['reviewer']
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_bank_account' in d:
            o.seller_bank_account = d['seller_bank_account']
        if 'seller_bank_name' in d:
            o.seller_bank_name = d['seller_bank_name']
        if 'seller_company_name' in d:
            o.seller_company_name = d['seller_company_name']
        if 'seller_inst_id' in d:
            o.seller_inst_id = d['seller_inst_id']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'seller_telephone' in d:
            o.seller_telephone = d['seller_telephone']
        if 'tax_amt' in d:
            o.tax_amt = d['tax_amt']
        if 'template_url' in d:
            o.template_url = d['template_url']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


