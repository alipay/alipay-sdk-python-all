#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceMerchantItem import InvoiceMerchantItem


class AlipayCommerceEcInvoiceConsumeApplyModel(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._buyer_address = None
        self._buyer_bank_account = None
        self._buyer_bank_name = None
        self._buyer_name = None
        self._buyer_tax_no = None
        self._buyer_tel = None
        self._enterprise_id = None
        self._invoice_item_list = None
        self._invoice_kind = None
        self._invoice_red_reason = None
        self._invoice_type = None
        self._outer_apply_id = None
        self._related_blue_invoice_no = None
        self._remark = None
        self._seller_enterprise_id = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
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
    def buyer_tel(self):
        return self._buyer_tel

    @buyer_tel.setter
    def buyer_tel(self, value):
        self._buyer_tel = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def invoice_item_list(self):
        return self._invoice_item_list

    @invoice_item_list.setter
    def invoice_item_list(self, value):
        if isinstance(value, list):
            self._invoice_item_list = list()
            for i in value:
                if isinstance(i, InvoiceMerchantItem):
                    self._invoice_item_list.append(i)
                else:
                    self._invoice_item_list.append(InvoiceMerchantItem.from_alipay_dict(i))
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
    def outer_apply_id(self):
        return self._outer_apply_id

    @outer_apply_id.setter
    def outer_apply_id(self, value):
        self._outer_apply_id = value
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
    def seller_enterprise_id(self):
        return self._seller_enterprise_id

    @seller_enterprise_id.setter
    def seller_enterprise_id(self, value):
        self._seller_enterprise_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
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
        if self.buyer_tel:
            if hasattr(self.buyer_tel, 'to_alipay_dict'):
                params['buyer_tel'] = self.buyer_tel.to_alipay_dict()
            else:
                params['buyer_tel'] = self.buyer_tel
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
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
        if self.outer_apply_id:
            if hasattr(self.outer_apply_id, 'to_alipay_dict'):
                params['outer_apply_id'] = self.outer_apply_id.to_alipay_dict()
            else:
                params['outer_apply_id'] = self.outer_apply_id
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
        if self.seller_enterprise_id:
            if hasattr(self.seller_enterprise_id, 'to_alipay_dict'):
                params['seller_enterprise_id'] = self.seller_enterprise_id.to_alipay_dict()
            else:
                params['seller_enterprise_id'] = self.seller_enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcInvoiceConsumeApplyModel()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
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
        if 'buyer_tel' in d:
            o.buyer_tel = d['buyer_tel']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'invoice_item_list' in d:
            o.invoice_item_list = d['invoice_item_list']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_red_reason' in d:
            o.invoice_red_reason = d['invoice_red_reason']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'outer_apply_id' in d:
            o.outer_apply_id = d['outer_apply_id']
        if 'related_blue_invoice_no' in d:
            o.related_blue_invoice_no = d['related_blue_invoice_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'seller_enterprise_id' in d:
            o.seller_enterprise_id = d['seller_enterprise_id']
        return o


