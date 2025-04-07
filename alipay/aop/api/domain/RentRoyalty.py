#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentRoyalty(object):

    def __init__(self):
        self._biz_order_id = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._current_buyout_after_price = None
        self._current_buyout_price = None
        self._expect_royalty_time = None
        self._out_order_id = None
        self._period = None
        self._royalty_after_price = None
        self._royalty_deliver_type = None
        self._royalty_installment_no = None
        self._royalty_price = None
        self._royalty_status = None
        self._royalty_time = None
        self._royalty_trigger_type = None
        self._settle_serial_no = None
        self._stage = None
        self._trade_no = None
        self._type = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def current_buyout_after_price(self):
        return self._current_buyout_after_price

    @current_buyout_after_price.setter
    def current_buyout_after_price(self, value):
        self._current_buyout_after_price = value
    @property
    def current_buyout_price(self):
        return self._current_buyout_price

    @current_buyout_price.setter
    def current_buyout_price(self, value):
        self._current_buyout_price = value
    @property
    def expect_royalty_time(self):
        return self._expect_royalty_time

    @expect_royalty_time.setter
    def expect_royalty_time(self, value):
        self._expect_royalty_time = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def royalty_after_price(self):
        return self._royalty_after_price

    @royalty_after_price.setter
    def royalty_after_price(self, value):
        self._royalty_after_price = value
    @property
    def royalty_deliver_type(self):
        return self._royalty_deliver_type

    @royalty_deliver_type.setter
    def royalty_deliver_type(self, value):
        self._royalty_deliver_type = value
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
    def royalty_status(self):
        return self._royalty_status

    @royalty_status.setter
    def royalty_status(self, value):
        self._royalty_status = value
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
    def settle_serial_no(self):
        return self._settle_serial_no

    @settle_serial_no.setter
    def settle_serial_no(self, value):
        self._settle_serial_no = value
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
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.current_buyout_after_price:
            if hasattr(self.current_buyout_after_price, 'to_alipay_dict'):
                params['current_buyout_after_price'] = self.current_buyout_after_price.to_alipay_dict()
            else:
                params['current_buyout_after_price'] = self.current_buyout_after_price
        if self.current_buyout_price:
            if hasattr(self.current_buyout_price, 'to_alipay_dict'):
                params['current_buyout_price'] = self.current_buyout_price.to_alipay_dict()
            else:
                params['current_buyout_price'] = self.current_buyout_price
        if self.expect_royalty_time:
            if hasattr(self.expect_royalty_time, 'to_alipay_dict'):
                params['expect_royalty_time'] = self.expect_royalty_time.to_alipay_dict()
            else:
                params['expect_royalty_time'] = self.expect_royalty_time
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.royalty_after_price:
            if hasattr(self.royalty_after_price, 'to_alipay_dict'):
                params['royalty_after_price'] = self.royalty_after_price.to_alipay_dict()
            else:
                params['royalty_after_price'] = self.royalty_after_price
        if self.royalty_deliver_type:
            if hasattr(self.royalty_deliver_type, 'to_alipay_dict'):
                params['royalty_deliver_type'] = self.royalty_deliver_type.to_alipay_dict()
            else:
                params['royalty_deliver_type'] = self.royalty_deliver_type
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
        if self.royalty_status:
            if hasattr(self.royalty_status, 'to_alipay_dict'):
                params['royalty_status'] = self.royalty_status.to_alipay_dict()
            else:
                params['royalty_status'] = self.royalty_status
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
        if self.settle_serial_no:
            if hasattr(self.settle_serial_no, 'to_alipay_dict'):
                params['settle_serial_no'] = self.settle_serial_no.to_alipay_dict()
            else:
                params['settle_serial_no'] = self.settle_serial_no
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
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRoyalty()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'current_buyout_after_price' in d:
            o.current_buyout_after_price = d['current_buyout_after_price']
        if 'current_buyout_price' in d:
            o.current_buyout_price = d['current_buyout_price']
        if 'expect_royalty_time' in d:
            o.expect_royalty_time = d['expect_royalty_time']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'period' in d:
            o.period = d['period']
        if 'royalty_after_price' in d:
            o.royalty_after_price = d['royalty_after_price']
        if 'royalty_deliver_type' in d:
            o.royalty_deliver_type = d['royalty_deliver_type']
        if 'royalty_installment_no' in d:
            o.royalty_installment_no = d['royalty_installment_no']
        if 'royalty_price' in d:
            o.royalty_price = d['royalty_price']
        if 'royalty_status' in d:
            o.royalty_status = d['royalty_status']
        if 'royalty_time' in d:
            o.royalty_time = d['royalty_time']
        if 'royalty_trigger_type' in d:
            o.royalty_trigger_type = d['royalty_trigger_type']
        if 'settle_serial_no' in d:
            o.settle_serial_no = d['settle_serial_no']
        if 'stage' in d:
            o.stage = d['stage']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'type' in d:
            o.type = d['type']
        return o


