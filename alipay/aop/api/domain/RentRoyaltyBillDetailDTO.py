#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentRoyaltyBillDetailDTO(object):

    def __init__(self):
        self._fund_type = None
        self._invest_account_type = None
        self._invest_card_no = None
        self._period = None
        self._royalty_bill_id = None
        self._royalty_deliver_type = None
        self._royalty_finish_time = None
        self._royalty_installment_no = None
        self._royalty_price = None
        self._stage = None
        self._trade_no = None

    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def invest_account_type(self):
        return self._invest_account_type

    @invest_account_type.setter
    def invest_account_type(self, value):
        self._invest_account_type = value
    @property
    def invest_card_no(self):
        return self._invest_card_no

    @invest_card_no.setter
    def invest_card_no(self, value):
        self._invest_card_no = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def royalty_bill_id(self):
        return self._royalty_bill_id

    @royalty_bill_id.setter
    def royalty_bill_id(self, value):
        self._royalty_bill_id = value
    @property
    def royalty_deliver_type(self):
        return self._royalty_deliver_type

    @royalty_deliver_type.setter
    def royalty_deliver_type(self, value):
        self._royalty_deliver_type = value
    @property
    def royalty_finish_time(self):
        return self._royalty_finish_time

    @royalty_finish_time.setter
    def royalty_finish_time(self, value):
        self._royalty_finish_time = value
    @property
    def royalty_installment_no(self):
        return self._royalty_installment_no

    @royalty_installment_no.setter
    def royalty_installment_no(self, value):
        self._royalty_installment_no = value
    @property
    def royalty_price(self):
        return self._royalty_price

    @royalty_price.setter
    def royalty_price(self, value):
        self._royalty_price = value
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
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.invest_account_type:
            if hasattr(self.invest_account_type, 'to_alipay_dict'):
                params['invest_account_type'] = self.invest_account_type.to_alipay_dict()
            else:
                params['invest_account_type'] = self.invest_account_type
        if self.invest_card_no:
            if hasattr(self.invest_card_no, 'to_alipay_dict'):
                params['invest_card_no'] = self.invest_card_no.to_alipay_dict()
            else:
                params['invest_card_no'] = self.invest_card_no
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.royalty_bill_id:
            if hasattr(self.royalty_bill_id, 'to_alipay_dict'):
                params['royalty_bill_id'] = self.royalty_bill_id.to_alipay_dict()
            else:
                params['royalty_bill_id'] = self.royalty_bill_id
        if self.royalty_deliver_type:
            if hasattr(self.royalty_deliver_type, 'to_alipay_dict'):
                params['royalty_deliver_type'] = self.royalty_deliver_type.to_alipay_dict()
            else:
                params['royalty_deliver_type'] = self.royalty_deliver_type
        if self.royalty_finish_time:
            if hasattr(self.royalty_finish_time, 'to_alipay_dict'):
                params['royalty_finish_time'] = self.royalty_finish_time.to_alipay_dict()
            else:
                params['royalty_finish_time'] = self.royalty_finish_time
        if self.royalty_installment_no:
            if hasattr(self.royalty_installment_no, 'to_alipay_dict'):
                params['royalty_installment_no'] = self.royalty_installment_no.to_alipay_dict()
            else:
                params['royalty_installment_no'] = self.royalty_installment_no
        if self.royalty_price:
            if hasattr(self.royalty_price, 'to_alipay_dict'):
                params['royalty_price'] = self.royalty_price.to_alipay_dict()
            else:
                params['royalty_price'] = self.royalty_price
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
        o = RentRoyaltyBillDetailDTO()
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'invest_account_type' in d:
            o.invest_account_type = d['invest_account_type']
        if 'invest_card_no' in d:
            o.invest_card_no = d['invest_card_no']
        if 'period' in d:
            o.period = d['period']
        if 'royalty_bill_id' in d:
            o.royalty_bill_id = d['royalty_bill_id']
        if 'royalty_deliver_type' in d:
            o.royalty_deliver_type = d['royalty_deliver_type']
        if 'royalty_finish_time' in d:
            o.royalty_finish_time = d['royalty_finish_time']
        if 'royalty_installment_no' in d:
            o.royalty_installment_no = d['royalty_installment_no']
        if 'royalty_price' in d:
            o.royalty_price = d['royalty_price']
        if 'stage' in d:
            o.stage = d['stage']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


