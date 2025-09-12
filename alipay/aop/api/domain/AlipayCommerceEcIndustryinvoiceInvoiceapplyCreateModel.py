#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndustryInvoiceItemInfo import IndustryInvoiceItemInfo
from alipay.aop.api.domain.IndustryInvoiceRealPropertyBusiness import IndustryInvoiceRealPropertyBusiness
from alipay.aop.api.domain.IndustryInvoiceTradeInfo import IndustryInvoiceTradeInfo


class AlipayCommerceEcIndustryinvoiceInvoiceapplyCreateModel(object):

    def __init__(self):
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_tax_no_type = None
        self._buyer_tel = None
        self._checker = None
        self._clerk = None
        self._clerk_cert_no = None
        self._clerk_cert_type = None
        self._invoice_item_list = None
        self._invoice_kind = None
        self._invoice_red_reason = None
        self._invoice_type = None
        self._nature_person_cert_no = None
        self._nature_person_cert_type = None
        self._nature_person_country = None
        self._nature_person_flag = None
        self._outer_apply_id = None
        self._payee = None
        self._product_id = None
        self._real_property_business_list = None
        self._related_blue_invoice_no = None
        self._remark = None
        self._seller_address = None
        self._seller_bank_account = None
        self._seller_bank_name = None
        self._seller_tel = None
        self._show_buyer_bank_info = None
        self._show_seller_bank_info = None
        self._tax_no = None
        self._trade_list = None

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
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value
    @property
    def buyer_tax_no(self):
        return self._buyer_tax_no

    @buyer_tax_no.setter
    def buyer_tax_no(self, value):
        self._buyer_tax_no = value
    @property
    def buyer_tax_no_type(self):
        return self._buyer_tax_no_type

    @buyer_tax_no_type.setter
    def buyer_tax_no_type(self, value):
        self._buyer_tax_no_type = value
    @property
    def buyer_tel(self):
        return self._buyer_tel

    @buyer_tel.setter
    def buyer_tel(self, value):
        self._buyer_tel = value
    @property
    def checker(self):
        return self._checker

    @checker.setter
    def checker(self, value):
        self._checker = value
    @property
    def clerk(self):
        return self._clerk

    @clerk.setter
    def clerk(self, value):
        self._clerk = value
    @property
    def clerk_cert_no(self):
        return self._clerk_cert_no

    @clerk_cert_no.setter
    def clerk_cert_no(self, value):
        self._clerk_cert_no = value
    @property
    def clerk_cert_type(self):
        return self._clerk_cert_type

    @clerk_cert_type.setter
    def clerk_cert_type(self, value):
        self._clerk_cert_type = value
    @property
    def invoice_item_list(self):
        return self._invoice_item_list

    @invoice_item_list.setter
    def invoice_item_list(self, value):
        if isinstance(value, list):
            self._invoice_item_list = list()
            for i in value:
                if isinstance(i, IndustryInvoiceItemInfo):
                    self._invoice_item_list.append(i)
                else:
                    self._invoice_item_list.append(IndustryInvoiceItemInfo.from_alipay_dict(i))
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def invoice_red_reason(self):
        return self._invoice_red_reason

    @invoice_red_reason.setter
    def invoice_red_reason(self, value):
        self._invoice_red_reason = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def nature_person_cert_no(self):
        return self._nature_person_cert_no

    @nature_person_cert_no.setter
    def nature_person_cert_no(self, value):
        self._nature_person_cert_no = value
    @property
    def nature_person_cert_type(self):
        return self._nature_person_cert_type

    @nature_person_cert_type.setter
    def nature_person_cert_type(self, value):
        self._nature_person_cert_type = value
    @property
    def nature_person_country(self):
        return self._nature_person_country

    @nature_person_country.setter
    def nature_person_country(self, value):
        self._nature_person_country = value
    @property
    def nature_person_flag(self):
        return self._nature_person_flag

    @nature_person_flag.setter
    def nature_person_flag(self, value):
        self._nature_person_flag = value
    @property
    def outer_apply_id(self):
        return self._outer_apply_id

    @outer_apply_id.setter
    def outer_apply_id(self, value):
        self._outer_apply_id = value
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self, value):
        self._payee = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def real_property_business_list(self):
        return self._real_property_business_list

    @real_property_business_list.setter
    def real_property_business_list(self, value):
        if isinstance(value, list):
            self._real_property_business_list = list()
            for i in value:
                if isinstance(i, IndustryInvoiceRealPropertyBusiness):
                    self._real_property_business_list.append(i)
                else:
                    self._real_property_business_list.append(IndustryInvoiceRealPropertyBusiness.from_alipay_dict(i))
    @property
    def related_blue_invoice_no(self):
        return self._related_blue_invoice_no

    @related_blue_invoice_no.setter
    def related_blue_invoice_no(self, value):
        self._related_blue_invoice_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
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
    def seller_tel(self):
        return self._seller_tel

    @seller_tel.setter
    def seller_tel(self, value):
        self._seller_tel = value
    @property
    def show_buyer_bank_info(self):
        return self._show_buyer_bank_info

    @show_buyer_bank_info.setter
    def show_buyer_bank_info(self, value):
        self._show_buyer_bank_info = value
    @property
    def show_seller_bank_info(self):
        return self._show_seller_bank_info

    @show_seller_bank_info.setter
    def show_seller_bank_info(self, value):
        self._show_seller_bank_info = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def trade_list(self):
        return self._trade_list

    @trade_list.setter
    def trade_list(self, value):
        if isinstance(value, list):
            self._trade_list = list()
            for i in value:
                if isinstance(i, IndustryInvoiceTradeInfo):
                    self._trade_list.append(i)
                else:
                    self._trade_list.append(IndustryInvoiceTradeInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
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
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        if self.buyer_tax_no:
            if hasattr(self.buyer_tax_no, 'to_alipay_dict'):
                params['buyer_tax_no'] = self.buyer_tax_no.to_alipay_dict()
            else:
                params['buyer_tax_no'] = self.buyer_tax_no
        if self.buyer_tax_no_type:
            if hasattr(self.buyer_tax_no_type, 'to_alipay_dict'):
                params['buyer_tax_no_type'] = self.buyer_tax_no_type.to_alipay_dict()
            else:
                params['buyer_tax_no_type'] = self.buyer_tax_no_type
        if self.buyer_tel:
            if hasattr(self.buyer_tel, 'to_alipay_dict'):
                params['buyer_tel'] = self.buyer_tel.to_alipay_dict()
            else:
                params['buyer_tel'] = self.buyer_tel
        if self.checker:
            if hasattr(self.checker, 'to_alipay_dict'):
                params['checker'] = self.checker.to_alipay_dict()
            else:
                params['checker'] = self.checker
        if self.clerk:
            if hasattr(self.clerk, 'to_alipay_dict'):
                params['clerk'] = self.clerk.to_alipay_dict()
            else:
                params['clerk'] = self.clerk
        if self.clerk_cert_no:
            if hasattr(self.clerk_cert_no, 'to_alipay_dict'):
                params['clerk_cert_no'] = self.clerk_cert_no.to_alipay_dict()
            else:
                params['clerk_cert_no'] = self.clerk_cert_no
        if self.clerk_cert_type:
            if hasattr(self.clerk_cert_type, 'to_alipay_dict'):
                params['clerk_cert_type'] = self.clerk_cert_type.to_alipay_dict()
            else:
                params['clerk_cert_type'] = self.clerk_cert_type
        if self.invoice_item_list:
            if isinstance(self.invoice_item_list, list):
                for i in range(0, len(self.invoice_item_list)):
                    element = self.invoice_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_item_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_item_list, 'to_alipay_dict'):
                params['invoice_item_list'] = self.invoice_item_list.to_alipay_dict()
            else:
                params['invoice_item_list'] = self.invoice_item_list
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.invoice_red_reason:
            if hasattr(self.invoice_red_reason, 'to_alipay_dict'):
                params['invoice_red_reason'] = self.invoice_red_reason.to_alipay_dict()
            else:
                params['invoice_red_reason'] = self.invoice_red_reason
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.nature_person_cert_no:
            if hasattr(self.nature_person_cert_no, 'to_alipay_dict'):
                params['nature_person_cert_no'] = self.nature_person_cert_no.to_alipay_dict()
            else:
                params['nature_person_cert_no'] = self.nature_person_cert_no
        if self.nature_person_cert_type:
            if hasattr(self.nature_person_cert_type, 'to_alipay_dict'):
                params['nature_person_cert_type'] = self.nature_person_cert_type.to_alipay_dict()
            else:
                params['nature_person_cert_type'] = self.nature_person_cert_type
        if self.nature_person_country:
            if hasattr(self.nature_person_country, 'to_alipay_dict'):
                params['nature_person_country'] = self.nature_person_country.to_alipay_dict()
            else:
                params['nature_person_country'] = self.nature_person_country
        if self.nature_person_flag:
            if hasattr(self.nature_person_flag, 'to_alipay_dict'):
                params['nature_person_flag'] = self.nature_person_flag.to_alipay_dict()
            else:
                params['nature_person_flag'] = self.nature_person_flag
        if self.outer_apply_id:
            if hasattr(self.outer_apply_id, 'to_alipay_dict'):
                params['outer_apply_id'] = self.outer_apply_id.to_alipay_dict()
            else:
                params['outer_apply_id'] = self.outer_apply_id
        if self.payee:
            if hasattr(self.payee, 'to_alipay_dict'):
                params['payee'] = self.payee.to_alipay_dict()
            else:
                params['payee'] = self.payee
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.real_property_business_list:
            if isinstance(self.real_property_business_list, list):
                for i in range(0, len(self.real_property_business_list)):
                    element = self.real_property_business_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.real_property_business_list[i] = element.to_alipay_dict()
            if hasattr(self.real_property_business_list, 'to_alipay_dict'):
                params['real_property_business_list'] = self.real_property_business_list.to_alipay_dict()
            else:
                params['real_property_business_list'] = self.real_property_business_list
        if self.related_blue_invoice_no:
            if hasattr(self.related_blue_invoice_no, 'to_alipay_dict'):
                params['related_blue_invoice_no'] = self.related_blue_invoice_no.to_alipay_dict()
            else:
                params['related_blue_invoice_no'] = self.related_blue_invoice_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
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
        if self.seller_tel:
            if hasattr(self.seller_tel, 'to_alipay_dict'):
                params['seller_tel'] = self.seller_tel.to_alipay_dict()
            else:
                params['seller_tel'] = self.seller_tel
        if self.show_buyer_bank_info:
            if hasattr(self.show_buyer_bank_info, 'to_alipay_dict'):
                params['show_buyer_bank_info'] = self.show_buyer_bank_info.to_alipay_dict()
            else:
                params['show_buyer_bank_info'] = self.show_buyer_bank_info
        if self.show_seller_bank_info:
            if hasattr(self.show_seller_bank_info, 'to_alipay_dict'):
                params['show_seller_bank_info'] = self.show_seller_bank_info.to_alipay_dict()
            else:
                params['show_seller_bank_info'] = self.show_seller_bank_info
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.trade_list:
            if isinstance(self.trade_list, list):
                for i in range(0, len(self.trade_list)):
                    element = self.trade_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_list, 'to_alipay_dict'):
                params['trade_list'] = self.trade_list.to_alipay_dict()
            else:
                params['trade_list'] = self.trade_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcIndustryinvoiceInvoiceapplyCreateModel()
        if 'buyer_address' in d:
            o.buyer_address = d['buyer_address']
        if 'buyer_bank_account' in d:
            o.buyer_bank_account = d['buyer_bank_account']
        if 'buyer_bank_name' in d:
            o.buyer_bank_name = d['buyer_bank_name']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        if 'buyer_tax_no' in d:
            o.buyer_tax_no = d['buyer_tax_no']
        if 'buyer_tax_no_type' in d:
            o.buyer_tax_no_type = d['buyer_tax_no_type']
        if 'buyer_tel' in d:
            o.buyer_tel = d['buyer_tel']
        if 'checker' in d:
            o.checker = d['checker']
        if 'clerk' in d:
            o.clerk = d['clerk']
        if 'clerk_cert_no' in d:
            o.clerk_cert_no = d['clerk_cert_no']
        if 'clerk_cert_type' in d:
            o.clerk_cert_type = d['clerk_cert_type']
        if 'invoice_item_list' in d:
            o.invoice_item_list = d['invoice_item_list']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_red_reason' in d:
            o.invoice_red_reason = d['invoice_red_reason']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'nature_person_cert_no' in d:
            o.nature_person_cert_no = d['nature_person_cert_no']
        if 'nature_person_cert_type' in d:
            o.nature_person_cert_type = d['nature_person_cert_type']
        if 'nature_person_country' in d:
            o.nature_person_country = d['nature_person_country']
        if 'nature_person_flag' in d:
            o.nature_person_flag = d['nature_person_flag']
        if 'outer_apply_id' in d:
            o.outer_apply_id = d['outer_apply_id']
        if 'payee' in d:
            o.payee = d['payee']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'real_property_business_list' in d:
            o.real_property_business_list = d['real_property_business_list']
        if 'related_blue_invoice_no' in d:
            o.related_blue_invoice_no = d['related_blue_invoice_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'seller_address' in d:
            o.seller_address = d['seller_address']
        if 'seller_bank_account' in d:
            o.seller_bank_account = d['seller_bank_account']
        if 'seller_bank_name' in d:
            o.seller_bank_name = d['seller_bank_name']
        if 'seller_tel' in d:
            o.seller_tel = d['seller_tel']
        if 'show_buyer_bank_info' in d:
            o.show_buyer_bank_info = d['show_buyer_bank_info']
        if 'show_seller_bank_info' in d:
            o.show_seller_bank_info = d['show_seller_bank_info']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'trade_list' in d:
            o.trade_list = d['trade_list']
        return o


