#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObcInvoiceIssuerRequest import ObcInvoiceIssuerRequest
from alipay.aop.api.domain.ObcInvoiceApplyLineRequest import ObcInvoiceApplyLineRequest


class AnttechOceanbaseInvoiceApplyModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_type = None
        self._buyer = None
        self._creator_id = None
        self._currency_code = None
        self._finance_remarks = None
        self._invoice_amount = None
        self._invoice_remarks = None
        self._objects = None
        self._remarks = None
        self._seller_inst_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, ObcInvoiceIssuerRequest):
            self._buyer = value
        else:
            self._buyer = ObcInvoiceIssuerRequest.from_alipay_dict(value)
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def finance_remarks(self):
        return self._finance_remarks

    @finance_remarks.setter
    def finance_remarks(self, value):
        self._finance_remarks = value
    @property
    def invoice_amount(self):
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, value):
        self._invoice_amount = value
    @property
    def invoice_remarks(self):
        return self._invoice_remarks

    @invoice_remarks.setter
    def invoice_remarks(self, value):
        self._invoice_remarks = value
    @property
    def objects(self):
        return self._objects

    @objects.setter
    def objects(self, value):
        if isinstance(value, list):
            self._objects = list()
            for i in value:
                if isinstance(i, ObcInvoiceApplyLineRequest):
                    self._objects.append(i)
                else:
                    self._objects.append(ObcInvoiceApplyLineRequest.from_alipay_dict(i))
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value
    @property
    def seller_inst_id(self):
        return self._seller_inst_id

    @seller_inst_id.setter
    def seller_inst_id(self, value):
        self._seller_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.finance_remarks:
            if hasattr(self.finance_remarks, 'to_alipay_dict'):
                params['finance_remarks'] = self.finance_remarks.to_alipay_dict()
            else:
                params['finance_remarks'] = self.finance_remarks
        if self.invoice_amount:
            if hasattr(self.invoice_amount, 'to_alipay_dict'):
                params['invoice_amount'] = self.invoice_amount.to_alipay_dict()
            else:
                params['invoice_amount'] = self.invoice_amount
        if self.invoice_remarks:
            if hasattr(self.invoice_remarks, 'to_alipay_dict'):
                params['invoice_remarks'] = self.invoice_remarks.to_alipay_dict()
            else:
                params['invoice_remarks'] = self.invoice_remarks
        if self.objects:
            if isinstance(self.objects, list):
                for i in range(0, len(self.objects)):
                    element = self.objects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.objects[i] = element.to_alipay_dict()
            if hasattr(self.objects, 'to_alipay_dict'):
                params['objects'] = self.objects.to_alipay_dict()
            else:
                params['objects'] = self.objects
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        if self.seller_inst_id:
            if hasattr(self.seller_inst_id, 'to_alipay_dict'):
                params['seller_inst_id'] = self.seller_inst_id.to_alipay_dict()
            else:
                params['seller_inst_id'] = self.seller_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseInvoiceApplyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'finance_remarks' in d:
            o.finance_remarks = d['finance_remarks']
        if 'invoice_amount' in d:
            o.invoice_amount = d['invoice_amount']
        if 'invoice_remarks' in d:
            o.invoice_remarks = d['invoice_remarks']
        if 'objects' in d:
            o.objects = d['objects']
        if 'remarks' in d:
            o.remarks = d['remarks']
        if 'seller_inst_id' in d:
            o.seller_inst_id = d['seller_inst_id']
        return o


