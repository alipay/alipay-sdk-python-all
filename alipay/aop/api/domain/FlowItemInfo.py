#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemBenefit import ItemBenefit
from alipay.aop.api.domain.ItemFrequentQA import ItemFrequentQA
from alipay.aop.api.domain.ItemIntroduction import ItemIntroduction


class FlowItemInfo(object):

    def __init__(self):
        self._benefit_list = None
        self._cancel_note = None
        self._detail = None
        self._face = None
        self._flow_type = None
        self._frequent_qa_list = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._introduction_list = None
        self._isp = None
        self._name = None
        self._need_protocol = None
        self._over_month = None
        self._pay_type = None
        self._period = None
        self._persist = None
        self._price = None
        self._price_note = None
        self._province = None
        self._scope = None
        self._sms_code_length = None
        self._state = None
        self._subscribe_limit = None
        self._valid_time = None

    @property
    def benefit_list(self):
        return self._benefit_list

    @benefit_list.setter
    def benefit_list(self, value):
        if isinstance(value, list):
            self._benefit_list = list()
            for i in value:
                if isinstance(i, ItemBenefit):
                    self._benefit_list.append(i)
                else:
                    self._benefit_list.append(ItemBenefit.from_alipay_dict(i))
    @property
    def cancel_note(self):
        return self._cancel_note

    @cancel_note.setter
    def cancel_note(self, value):
        self._cancel_note = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, value):
        self._face = value
    @property
    def flow_type(self):
        return self._flow_type

    @flow_type.setter
    def flow_type(self, value):
        self._flow_type = value
    @property
    def frequent_qa_list(self):
        return self._frequent_qa_list

    @frequent_qa_list.setter
    def frequent_qa_list(self, value):
        if isinstance(value, list):
            self._frequent_qa_list = list()
            for i in value:
                if isinstance(i, ItemFrequentQA):
                    self._frequent_qa_list.append(i)
                else:
                    self._frequent_qa_list.append(ItemFrequentQA.from_alipay_dict(i))
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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def introduction_list(self):
        return self._introduction_list

    @introduction_list.setter
    def introduction_list(self, value):
        if isinstance(value, list):
            self._introduction_list = list()
            for i in value:
                if isinstance(i, ItemIntroduction):
                    self._introduction_list.append(i)
                else:
                    self._introduction_list.append(ItemIntroduction.from_alipay_dict(i))
    @property
    def isp(self):
        return self._isp

    @isp.setter
    def isp(self, value):
        self._isp = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def need_protocol(self):
        return self._need_protocol

    @need_protocol.setter
    def need_protocol(self, value):
        self._need_protocol = value
    @property
    def over_month(self):
        return self._over_month

    @over_month.setter
    def over_month(self, value):
        self._over_month = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def persist(self):
        return self._persist

    @persist.setter
    def persist(self, value):
        self._persist = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def price_note(self):
        return self._price_note

    @price_note.setter
    def price_note(self, value):
        self._price_note = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def sms_code_length(self):
        return self._sms_code_length

    @sms_code_length.setter
    def sms_code_length(self, value):
        self._sms_code_length = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def subscribe_limit(self):
        return self._subscribe_limit

    @subscribe_limit.setter
    def subscribe_limit(self, value):
        self._subscribe_limit = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_list:
            if isinstance(self.benefit_list, list):
                for i in range(0, len(self.benefit_list)):
                    element = self.benefit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_list[i] = element.to_alipay_dict()
            if hasattr(self.benefit_list, 'to_alipay_dict'):
                params['benefit_list'] = self.benefit_list.to_alipay_dict()
            else:
                params['benefit_list'] = self.benefit_list
        if self.cancel_note:
            if hasattr(self.cancel_note, 'to_alipay_dict'):
                params['cancel_note'] = self.cancel_note.to_alipay_dict()
            else:
                params['cancel_note'] = self.cancel_note
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.face:
            if hasattr(self.face, 'to_alipay_dict'):
                params['face'] = self.face.to_alipay_dict()
            else:
                params['face'] = self.face
        if self.flow_type:
            if hasattr(self.flow_type, 'to_alipay_dict'):
                params['flow_type'] = self.flow_type.to_alipay_dict()
            else:
                params['flow_type'] = self.flow_type
        if self.frequent_qa_list:
            if isinstance(self.frequent_qa_list, list):
                for i in range(0, len(self.frequent_qa_list)):
                    element = self.frequent_qa_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.frequent_qa_list[i] = element.to_alipay_dict()
            if hasattr(self.frequent_qa_list, 'to_alipay_dict'):
                params['frequent_qa_list'] = self.frequent_qa_list.to_alipay_dict()
            else:
                params['frequent_qa_list'] = self.frequent_qa_list
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
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.introduction_list:
            if isinstance(self.introduction_list, list):
                for i in range(0, len(self.introduction_list)):
                    element = self.introduction_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.introduction_list[i] = element.to_alipay_dict()
            if hasattr(self.introduction_list, 'to_alipay_dict'):
                params['introduction_list'] = self.introduction_list.to_alipay_dict()
            else:
                params['introduction_list'] = self.introduction_list
        if self.isp:
            if hasattr(self.isp, 'to_alipay_dict'):
                params['isp'] = self.isp.to_alipay_dict()
            else:
                params['isp'] = self.isp
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.need_protocol:
            if hasattr(self.need_protocol, 'to_alipay_dict'):
                params['need_protocol'] = self.need_protocol.to_alipay_dict()
            else:
                params['need_protocol'] = self.need_protocol
        if self.over_month:
            if hasattr(self.over_month, 'to_alipay_dict'):
                params['over_month'] = self.over_month.to_alipay_dict()
            else:
                params['over_month'] = self.over_month
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.persist:
            if hasattr(self.persist, 'to_alipay_dict'):
                params['persist'] = self.persist.to_alipay_dict()
            else:
                params['persist'] = self.persist
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.price_note:
            if hasattr(self.price_note, 'to_alipay_dict'):
                params['price_note'] = self.price_note.to_alipay_dict()
            else:
                params['price_note'] = self.price_note
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        if self.sms_code_length:
            if hasattr(self.sms_code_length, 'to_alipay_dict'):
                params['sms_code_length'] = self.sms_code_length.to_alipay_dict()
            else:
                params['sms_code_length'] = self.sms_code_length
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.subscribe_limit:
            if hasattr(self.subscribe_limit, 'to_alipay_dict'):
                params['subscribe_limit'] = self.subscribe_limit.to_alipay_dict()
            else:
                params['subscribe_limit'] = self.subscribe_limit
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FlowItemInfo()
        if 'benefit_list' in d:
            o.benefit_list = d['benefit_list']
        if 'cancel_note' in d:
            o.cancel_note = d['cancel_note']
        if 'detail' in d:
            o.detail = d['detail']
        if 'face' in d:
            o.face = d['face']
        if 'flow_type' in d:
            o.flow_type = d['flow_type']
        if 'frequent_qa_list' in d:
            o.frequent_qa_list = d['frequent_qa_list']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'introduction_list' in d:
            o.introduction_list = d['introduction_list']
        if 'isp' in d:
            o.isp = d['isp']
        if 'name' in d:
            o.name = d['name']
        if 'need_protocol' in d:
            o.need_protocol = d['need_protocol']
        if 'over_month' in d:
            o.over_month = d['over_month']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'period' in d:
            o.period = d['period']
        if 'persist' in d:
            o.persist = d['persist']
        if 'price' in d:
            o.price = d['price']
        if 'price_note' in d:
            o.price_note = d['price_note']
        if 'province' in d:
            o.province = d['province']
        if 'scope' in d:
            o.scope = d['scope']
        if 'sms_code_length' in d:
            o.sms_code_length = d['sms_code_length']
        if 'state' in d:
            o.state = d['state']
        if 'subscribe_limit' in d:
            o.subscribe_limit = d['subscribe_limit']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        return o


