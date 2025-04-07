#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderStatusSyncCancelInfoDTO import OrderStatusSyncCancelInfoDTO
from alipay.aop.api.domain.OrderStatusSyncConfirmationInfoDTO import OrderStatusSyncConfirmationInfoDTO


class AlipayCommerceHotelOrderstatusSyncModel(object):

    def __init__(self):
        self._alipay_hotel_order_id = None
        self._biz_time = None
        self._cancel_info = None
        self._confirmation_info = None
        self._open_id = None
        self._outer_order_id = None
        self._status = None

    @property
    def alipay_hotel_order_id(self):
        return self._alipay_hotel_order_id

    @alipay_hotel_order_id.setter
    def alipay_hotel_order_id(self, value):
        self._alipay_hotel_order_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def cancel_info(self):
        return self._cancel_info

    @cancel_info.setter
    def cancel_info(self, value):
        if isinstance(value, OrderStatusSyncCancelInfoDTO):
            self._cancel_info = value
        else:
            self._cancel_info = OrderStatusSyncCancelInfoDTO.from_alipay_dict(value)
    @property
    def confirmation_info(self):
        return self._confirmation_info

    @confirmation_info.setter
    def confirmation_info(self, value):
        if isinstance(value, OrderStatusSyncConfirmationInfoDTO):
            self._confirmation_info = value
        else:
            self._confirmation_info = OrderStatusSyncConfirmationInfoDTO.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def outer_order_id(self):
        return self._outer_order_id

    @outer_order_id.setter
    def outer_order_id(self, value):
        self._outer_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_hotel_order_id:
            if hasattr(self.alipay_hotel_order_id, 'to_alipay_dict'):
                params['alipay_hotel_order_id'] = self.alipay_hotel_order_id.to_alipay_dict()
            else:
                params['alipay_hotel_order_id'] = self.alipay_hotel_order_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.cancel_info:
            if hasattr(self.cancel_info, 'to_alipay_dict'):
                params['cancel_info'] = self.cancel_info.to_alipay_dict()
            else:
                params['cancel_info'] = self.cancel_info
        if self.confirmation_info:
            if hasattr(self.confirmation_info, 'to_alipay_dict'):
                params['confirmation_info'] = self.confirmation_info.to_alipay_dict()
            else:
                params['confirmation_info'] = self.confirmation_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.outer_order_id:
            if hasattr(self.outer_order_id, 'to_alipay_dict'):
                params['outer_order_id'] = self.outer_order_id.to_alipay_dict()
            else:
                params['outer_order_id'] = self.outer_order_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelOrderstatusSyncModel()
        if 'alipay_hotel_order_id' in d:
            o.alipay_hotel_order_id = d['alipay_hotel_order_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'cancel_info' in d:
            o.cancel_info = d['cancel_info']
        if 'confirmation_info' in d:
            o.confirmation_info = d['confirmation_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'outer_order_id' in d:
            o.outer_order_id = d['outer_order_id']
        if 'status' in d:
            o.status = d['status']
        return o


