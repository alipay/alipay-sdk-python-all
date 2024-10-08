#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrafficAirticketOrderCommodityInfo import TrafficAirticketOrderCommodityInfo
from alipay.aop.api.domain.TrafficAirticketOrderDiscountInfo import TrafficAirticketOrderDiscountInfo
from alipay.aop.api.domain.TrafficAirticketOrderPassengerInfo import TrafficAirticketOrderPassengerInfo


class AlipayCommerceTransportAirticketOrderSyncModel(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._biz_type = None
        self._buyer_openid = None
        self._buyer_uid = None
        self._commission_channel = None
        self._commodity_info_list = None
        self._create_time = None
        self._discount_amount = None
        self._discount_info_list = None
        self._link_page = None
        self._modified_time = None
        self._ori_out_biz_no = None
        self._out_biz_no = None
        self._passenger_info_list = None
        self._pay_amount = None
        self._source_channel = None
        self._source_channel_id = None
        self._status = None
        self._status_desc = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def buyer_openid(self):
        return self._buyer_openid

    @buyer_openid.setter
    def buyer_openid(self, value):
        self._buyer_openid = value
    @property
    def buyer_uid(self):
        return self._buyer_uid

    @buyer_uid.setter
    def buyer_uid(self, value):
        self._buyer_uid = value
    @property
    def commission_channel(self):
        return self._commission_channel

    @commission_channel.setter
    def commission_channel(self, value):
        self._commission_channel = value
    @property
    def commodity_info_list(self):
        return self._commodity_info_list

    @commodity_info_list.setter
    def commodity_info_list(self, value):
        if isinstance(value, list):
            self._commodity_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderCommodityInfo):
                    self._commodity_info_list.append(i)
                else:
                    self._commodity_info_list.append(TrafficAirticketOrderCommodityInfo.from_alipay_dict(i))
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_info_list(self):
        return self._discount_info_list

    @discount_info_list.setter
    def discount_info_list(self, value):
        if isinstance(value, list):
            self._discount_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderDiscountInfo):
                    self._discount_info_list.append(i)
                else:
                    self._discount_info_list.append(TrafficAirticketOrderDiscountInfo.from_alipay_dict(i))
    @property
    def link_page(self):
        return self._link_page

    @link_page.setter
    def link_page(self, value):
        self._link_page = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def ori_out_biz_no(self):
        return self._ori_out_biz_no

    @ori_out_biz_no.setter
    def ori_out_biz_no(self, value):
        self._ori_out_biz_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def passenger_info_list(self):
        return self._passenger_info_list

    @passenger_info_list.setter
    def passenger_info_list(self, value):
        if isinstance(value, list):
            self._passenger_info_list = list()
            for i in value:
                if isinstance(i, TrafficAirticketOrderPassengerInfo):
                    self._passenger_info_list.append(i)
                else:
                    self._passenger_info_list.append(TrafficAirticketOrderPassengerInfo.from_alipay_dict(i))
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def source_channel(self):
        return self._source_channel

    @source_channel.setter
    def source_channel(self, value):
        self._source_channel = value
    @property
    def source_channel_id(self):
        return self._source_channel_id

    @source_channel_id.setter
    def source_channel_id(self, value):
        self._source_channel_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.buyer_openid:
            if hasattr(self.buyer_openid, 'to_alipay_dict'):
                params['buyer_openid'] = self.buyer_openid.to_alipay_dict()
            else:
                params['buyer_openid'] = self.buyer_openid
        if self.buyer_uid:
            if hasattr(self.buyer_uid, 'to_alipay_dict'):
                params['buyer_uid'] = self.buyer_uid.to_alipay_dict()
            else:
                params['buyer_uid'] = self.buyer_uid
        if self.commission_channel:
            if hasattr(self.commission_channel, 'to_alipay_dict'):
                params['commission_channel'] = self.commission_channel.to_alipay_dict()
            else:
                params['commission_channel'] = self.commission_channel
        if self.commodity_info_list:
            if isinstance(self.commodity_info_list, list):
                for i in range(0, len(self.commodity_info_list)):
                    element = self.commodity_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commodity_info_list[i] = element.to_alipay_dict()
            if hasattr(self.commodity_info_list, 'to_alipay_dict'):
                params['commodity_info_list'] = self.commodity_info_list.to_alipay_dict()
            else:
                params['commodity_info_list'] = self.commodity_info_list
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_info_list:
            if isinstance(self.discount_info_list, list):
                for i in range(0, len(self.discount_info_list)):
                    element = self.discount_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_info_list[i] = element.to_alipay_dict()
            if hasattr(self.discount_info_list, 'to_alipay_dict'):
                params['discount_info_list'] = self.discount_info_list.to_alipay_dict()
            else:
                params['discount_info_list'] = self.discount_info_list
        if self.link_page:
            if hasattr(self.link_page, 'to_alipay_dict'):
                params['link_page'] = self.link_page.to_alipay_dict()
            else:
                params['link_page'] = self.link_page
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.ori_out_biz_no:
            if hasattr(self.ori_out_biz_no, 'to_alipay_dict'):
                params['ori_out_biz_no'] = self.ori_out_biz_no.to_alipay_dict()
            else:
                params['ori_out_biz_no'] = self.ori_out_biz_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.passenger_info_list:
            if isinstance(self.passenger_info_list, list):
                for i in range(0, len(self.passenger_info_list)):
                    element = self.passenger_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.passenger_info_list[i] = element.to_alipay_dict()
            if hasattr(self.passenger_info_list, 'to_alipay_dict'):
                params['passenger_info_list'] = self.passenger_info_list.to_alipay_dict()
            else:
                params['passenger_info_list'] = self.passenger_info_list
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.source_channel:
            if hasattr(self.source_channel, 'to_alipay_dict'):
                params['source_channel'] = self.source_channel.to_alipay_dict()
            else:
                params['source_channel'] = self.source_channel
        if self.source_channel_id:
            if hasattr(self.source_channel_id, 'to_alipay_dict'):
                params['source_channel_id'] = self.source_channel_id.to_alipay_dict()
            else:
                params['source_channel_id'] = self.source_channel_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
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
        o = AlipayCommerceTransportAirticketOrderSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'buyer_openid' in d:
            o.buyer_openid = d['buyer_openid']
        if 'buyer_uid' in d:
            o.buyer_uid = d['buyer_uid']
        if 'commission_channel' in d:
            o.commission_channel = d['commission_channel']
        if 'commodity_info_list' in d:
            o.commodity_info_list = d['commodity_info_list']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_info_list' in d:
            o.discount_info_list = d['discount_info_list']
        if 'link_page' in d:
            o.link_page = d['link_page']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'ori_out_biz_no' in d:
            o.ori_out_biz_no = d['ori_out_biz_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'passenger_info_list' in d:
            o.passenger_info_list = d['passenger_info_list']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'source_channel' in d:
            o.source_channel = d['source_channel']
        if 'source_channel_id' in d:
            o.source_channel_id = d['source_channel_id']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


