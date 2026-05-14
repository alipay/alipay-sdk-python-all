#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExaminationBookInfo import ExaminationBookInfo
from alipay.aop.api.domain.ExaminationCheckInfo import ExaminationCheckInfo
from alipay.aop.api.domain.ExaminationDeliverInfo import ExaminationDeliverInfo
from alipay.aop.api.domain.ExaminationItemVO import ExaminationItemVO
from alipay.aop.api.domain.ExaminationPayInfo import ExaminationPayInfo


class Examination(object):

    def __init__(self):
        self._application_id = None
        self._book_info = None
        self._check_info = None
        self._deliver_info = None
        self._fulfillment_status = None
        self._items = None
        self._order_no = None
        self._pay_info = None
        self._relation_order_no = None
        self._seller_code = None
        self._source = None
        self._store_code = None
        self._store_id = None
        self._store_name = None
        self._unique_no = None

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def book_info(self):
        return self._book_info

    @book_info.setter
    def book_info(self, value):
        if isinstance(value, ExaminationBookInfo):
            self._book_info = value
        else:
            self._book_info = ExaminationBookInfo.from_alipay_dict(value)
    @property
    def check_info(self):
        return self._check_info

    @check_info.setter
    def check_info(self, value):
        if isinstance(value, ExaminationCheckInfo):
            self._check_info = value
        else:
            self._check_info = ExaminationCheckInfo.from_alipay_dict(value)
    @property
    def deliver_info(self):
        return self._deliver_info

    @deliver_info.setter
    def deliver_info(self, value):
        if isinstance(value, ExaminationDeliverInfo):
            self._deliver_info = value
        else:
            self._deliver_info = ExaminationDeliverInfo.from_alipay_dict(value)
    @property
    def fulfillment_status(self):
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, value):
        self._fulfillment_status = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, ExaminationItemVO):
                    self._items.append(i)
                else:
                    self._items.append(ExaminationItemVO.from_alipay_dict(i))
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_info(self):
        return self._pay_info

    @pay_info.setter
    def pay_info(self, value):
        if isinstance(value, ExaminationPayInfo):
            self._pay_info = value
        else:
            self._pay_info = ExaminationPayInfo.from_alipay_dict(value)
    @property
    def relation_order_no(self):
        return self._relation_order_no

    @relation_order_no.setter
    def relation_order_no(self, value):
        self._relation_order_no = value
    @property
    def seller_code(self):
        return self._seller_code

    @seller_code.setter
    def seller_code(self, value):
        self._seller_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def unique_no(self):
        return self._unique_no

    @unique_no.setter
    def unique_no(self, value):
        self._unique_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.book_info:
            if hasattr(self.book_info, 'to_alipay_dict'):
                params['book_info'] = self.book_info.to_alipay_dict()
            else:
                params['book_info'] = self.book_info
        if self.check_info:
            if hasattr(self.check_info, 'to_alipay_dict'):
                params['check_info'] = self.check_info.to_alipay_dict()
            else:
                params['check_info'] = self.check_info
        if self.deliver_info:
            if hasattr(self.deliver_info, 'to_alipay_dict'):
                params['deliver_info'] = self.deliver_info.to_alipay_dict()
            else:
                params['deliver_info'] = self.deliver_info
        if self.fulfillment_status:
            if hasattr(self.fulfillment_status, 'to_alipay_dict'):
                params['fulfillment_status'] = self.fulfillment_status.to_alipay_dict()
            else:
                params['fulfillment_status'] = self.fulfillment_status
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pay_info:
            if hasattr(self.pay_info, 'to_alipay_dict'):
                params['pay_info'] = self.pay_info.to_alipay_dict()
            else:
                params['pay_info'] = self.pay_info
        if self.relation_order_no:
            if hasattr(self.relation_order_no, 'to_alipay_dict'):
                params['relation_order_no'] = self.relation_order_no.to_alipay_dict()
            else:
                params['relation_order_no'] = self.relation_order_no
        if self.seller_code:
            if hasattr(self.seller_code, 'to_alipay_dict'):
                params['seller_code'] = self.seller_code.to_alipay_dict()
            else:
                params['seller_code'] = self.seller_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.unique_no:
            if hasattr(self.unique_no, 'to_alipay_dict'):
                params['unique_no'] = self.unique_no.to_alipay_dict()
            else:
                params['unique_no'] = self.unique_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Examination()
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'book_info' in d:
            o.book_info = d['book_info']
        if 'check_info' in d:
            o.check_info = d['check_info']
        if 'deliver_info' in d:
            o.deliver_info = d['deliver_info']
        if 'fulfillment_status' in d:
            o.fulfillment_status = d['fulfillment_status']
        if 'items' in d:
            o.items = d['items']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_info' in d:
            o.pay_info = d['pay_info']
        if 'relation_order_no' in d:
            o.relation_order_no = d['relation_order_no']
        if 'seller_code' in d:
            o.seller_code = d['seller_code']
        if 'source' in d:
            o.source = d['source']
        if 'store_code' in d:
            o.store_code = d['store_code']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'unique_no' in d:
            o.unique_no = d['unique_no']
        return o


