#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentBillRoyaltyDto import RentBillRoyaltyDto


class RentBillRoyaltyDetailDto(object):

    def __init__(self):
        self._actual_royalty_amount = None
        self._biz_order_id = None
        self._invest_id = None
        self._period = None
        self._rent_royalty_list = None
        self._royalty_deliver_type = None
        self._royalty_id = None
        self._royalty_installment_no = None
        self._royalty_payment_method = None
        self._royalty_payment_method_note = None
        self._royalty_time = None
        self._royalty_trigger_type = None
        self._seller_id = None
        self._special_royalty_type = None
        self._stage = None
        self._trade_no = None

    @property
    def actual_royalty_amount(self):
        return self._actual_royalty_amount

    @actual_royalty_amount.setter
    def actual_royalty_amount(self, value):
        self._actual_royalty_amount = value
    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def invest_id(self):
        return self._invest_id

    @invest_id.setter
    def invest_id(self, value):
        self._invest_id = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def rent_royalty_list(self):
        return self._rent_royalty_list

    @rent_royalty_list.setter
    def rent_royalty_list(self, value):
        if isinstance(value, list):
            self._rent_royalty_list = list()
            for i in value:
                if isinstance(i, RentBillRoyaltyDto):
                    self._rent_royalty_list.append(i)
                else:
                    self._rent_royalty_list.append(RentBillRoyaltyDto.from_alipay_dict(i))
    @property
    def royalty_deliver_type(self):
        return self._royalty_deliver_type

    @royalty_deliver_type.setter
    def royalty_deliver_type(self, value):
        self._royalty_deliver_type = value
    @property
    def royalty_id(self):
        return self._royalty_id

    @royalty_id.setter
    def royalty_id(self, value):
        self._royalty_id = value
    @property
    def royalty_installment_no(self):
        return self._royalty_installment_no

    @royalty_installment_no.setter
    def royalty_installment_no(self, value):
        self._royalty_installment_no = value
    @property
    def royalty_payment_method(self):
        return self._royalty_payment_method

    @royalty_payment_method.setter
    def royalty_payment_method(self, value):
        self._royalty_payment_method = value
    @property
    def royalty_payment_method_note(self):
        return self._royalty_payment_method_note

    @royalty_payment_method_note.setter
    def royalty_payment_method_note(self, value):
        self._royalty_payment_method_note = value
    @property
    def royalty_time(self):
        return self._royalty_time

    @royalty_time.setter
    def royalty_time(self, value):
        self._royalty_time = value
    @property
    def royalty_trigger_type(self):
        return self._royalty_trigger_type

    @royalty_trigger_type.setter
    def royalty_trigger_type(self, value):
        self._royalty_trigger_type = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def special_royalty_type(self):
        return self._special_royalty_type

    @special_royalty_type.setter
    def special_royalty_type(self, value):
        self._special_royalty_type = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_royalty_amount:
            if hasattr(self.actual_royalty_amount, 'to_alipay_dict'):
                params['actual_royalty_amount'] = self.actual_royalty_amount.to_alipay_dict()
            else:
                params['actual_royalty_amount'] = self.actual_royalty_amount
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.invest_id:
            if hasattr(self.invest_id, 'to_alipay_dict'):
                params['invest_id'] = self.invest_id.to_alipay_dict()
            else:
                params['invest_id'] = self.invest_id
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.rent_royalty_list:
            if isinstance(self.rent_royalty_list, list):
                for i in range(0, len(self.rent_royalty_list)):
                    element = self.rent_royalty_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rent_royalty_list[i] = element.to_alipay_dict()
            if hasattr(self.rent_royalty_list, 'to_alipay_dict'):
                params['rent_royalty_list'] = self.rent_royalty_list.to_alipay_dict()
            else:
                params['rent_royalty_list'] = self.rent_royalty_list
        if self.royalty_deliver_type:
            if hasattr(self.royalty_deliver_type, 'to_alipay_dict'):
                params['royalty_deliver_type'] = self.royalty_deliver_type.to_alipay_dict()
            else:
                params['royalty_deliver_type'] = self.royalty_deliver_type
        if self.royalty_id:
            if hasattr(self.royalty_id, 'to_alipay_dict'):
                params['royalty_id'] = self.royalty_id.to_alipay_dict()
            else:
                params['royalty_id'] = self.royalty_id
        if self.royalty_installment_no:
            if hasattr(self.royalty_installment_no, 'to_alipay_dict'):
                params['royalty_installment_no'] = self.royalty_installment_no.to_alipay_dict()
            else:
                params['royalty_installment_no'] = self.royalty_installment_no
        if self.royalty_payment_method:
            if hasattr(self.royalty_payment_method, 'to_alipay_dict'):
                params['royalty_payment_method'] = self.royalty_payment_method.to_alipay_dict()
            else:
                params['royalty_payment_method'] = self.royalty_payment_method
        if self.royalty_payment_method_note:
            if hasattr(self.royalty_payment_method_note, 'to_alipay_dict'):
                params['royalty_payment_method_note'] = self.royalty_payment_method_note.to_alipay_dict()
            else:
                params['royalty_payment_method_note'] = self.royalty_payment_method_note
        if self.royalty_time:
            if hasattr(self.royalty_time, 'to_alipay_dict'):
                params['royalty_time'] = self.royalty_time.to_alipay_dict()
            else:
                params['royalty_time'] = self.royalty_time
        if self.royalty_trigger_type:
            if hasattr(self.royalty_trigger_type, 'to_alipay_dict'):
                params['royalty_trigger_type'] = self.royalty_trigger_type.to_alipay_dict()
            else:
                params['royalty_trigger_type'] = self.royalty_trigger_type
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.special_royalty_type:
            if hasattr(self.special_royalty_type, 'to_alipay_dict'):
                params['special_royalty_type'] = self.special_royalty_type.to_alipay_dict()
            else:
                params['special_royalty_type'] = self.special_royalty_type
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentBillRoyaltyDetailDto()
        if 'actual_royalty_amount' in d:
            o.actual_royalty_amount = d['actual_royalty_amount']
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'invest_id' in d:
            o.invest_id = d['invest_id']
        if 'period' in d:
            o.period = d['period']
        if 'rent_royalty_list' in d:
            o.rent_royalty_list = d['rent_royalty_list']
        if 'royalty_deliver_type' in d:
            o.royalty_deliver_type = d['royalty_deliver_type']
        if 'royalty_id' in d:
            o.royalty_id = d['royalty_id']
        if 'royalty_installment_no' in d:
            o.royalty_installment_no = d['royalty_installment_no']
        if 'royalty_payment_method' in d:
            o.royalty_payment_method = d['royalty_payment_method']
        if 'royalty_payment_method_note' in d:
            o.royalty_payment_method_note = d['royalty_payment_method_note']
        if 'royalty_time' in d:
            o.royalty_time = d['royalty_time']
        if 'royalty_trigger_type' in d:
            o.royalty_trigger_type = d['royalty_trigger_type']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'special_royalty_type' in d:
            o.special_royalty_type = d['special_royalty_type']
        if 'stage' in d:
            o.stage = d['stage']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


