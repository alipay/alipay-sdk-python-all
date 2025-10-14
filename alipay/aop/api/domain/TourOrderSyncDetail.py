#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TourVoucherDetail import TourVoucherDetail


class TourOrderSyncDetail(object):

    def __init__(self):
        self._biz_source_num = None
        self._cert_no = None
        self._name = None
        self._order_amount = None
        self._order_info = None
        self._order_status = None
        self._out_biz_no = None
        self._project_id = None
        self._scene_type = None
        self._tele_no = None
        self._tour_voucher_list = None
        self._trade_no = None

    @property
    def biz_source_num(self):
        return self._biz_source_num

    @biz_source_num.setter
    def biz_source_num(self, value):
        self._biz_source_num = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        self._order_info = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def tele_no(self):
        return self._tele_no

    @tele_no.setter
    def tele_no(self, value):
        self._tele_no = value
    @property
    def tour_voucher_list(self):
        return self._tour_voucher_list

    @tour_voucher_list.setter
    def tour_voucher_list(self, value):
        if isinstance(value, list):
            self._tour_voucher_list = list()
            for i in value:
                if isinstance(i, TourVoucherDetail):
                    self._tour_voucher_list.append(i)
                else:
                    self._tour_voucher_list.append(TourVoucherDetail.from_alipay_dict(i))
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source_num:
            if hasattr(self.biz_source_num, 'to_alipay_dict'):
                params['biz_source_num'] = self.biz_source_num.to_alipay_dict()
            else:
                params['biz_source_num'] = self.biz_source_num
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.tele_no:
            if hasattr(self.tele_no, 'to_alipay_dict'):
                params['tele_no'] = self.tele_no.to_alipay_dict()
            else:
                params['tele_no'] = self.tele_no
        if self.tour_voucher_list:
            if isinstance(self.tour_voucher_list, list):
                for i in range(0, len(self.tour_voucher_list)):
                    element = self.tour_voucher_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tour_voucher_list[i] = element.to_alipay_dict()
            if hasattr(self.tour_voucher_list, 'to_alipay_dict'):
                params['tour_voucher_list'] = self.tour_voucher_list.to_alipay_dict()
            else:
                params['tour_voucher_list'] = self.tour_voucher_list
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
        o = TourOrderSyncDetail()
        if 'biz_source_num' in d:
            o.biz_source_num = d['biz_source_num']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'name' in d:
            o.name = d['name']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'tele_no' in d:
            o.tele_no = d['tele_no']
        if 'tour_voucher_list' in d:
            o.tour_voucher_list = d['tour_voucher_list']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


