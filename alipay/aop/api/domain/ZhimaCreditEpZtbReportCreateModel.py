#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpZtbReportCreateModel(object):

    def __init__(self):
        self._bid_type = None
        self._bidder_ep_cert_no = None
        self._bidder_ep_name = None
        self._bidding_ep_cert_no = None
        self._bidding_ep_name = None
        self._heading_object = None
        self._out_biz_no = None
        self._project_area_code = None
        self._project_area_desc = None
        self._project_budget = None
        self._project_name = None
        self._scene_code = None
        self._text_object = None

    @property
    def bid_type(self):
        return self._bid_type

    @bid_type.setter
    def bid_type(self, value):
        self._bid_type = value
    @property
    def bidder_ep_cert_no(self):
        return self._bidder_ep_cert_no

    @bidder_ep_cert_no.setter
    def bidder_ep_cert_no(self, value):
        self._bidder_ep_cert_no = value
    @property
    def bidder_ep_name(self):
        return self._bidder_ep_name

    @bidder_ep_name.setter
    def bidder_ep_name(self, value):
        self._bidder_ep_name = value
    @property
    def bidding_ep_cert_no(self):
        return self._bidding_ep_cert_no

    @bidding_ep_cert_no.setter
    def bidding_ep_cert_no(self, value):
        self._bidding_ep_cert_no = value
    @property
    def bidding_ep_name(self):
        return self._bidding_ep_name

    @bidding_ep_name.setter
    def bidding_ep_name(self, value):
        self._bidding_ep_name = value
    @property
    def heading_object(self):
        return self._heading_object

    @heading_object.setter
    def heading_object(self, value):
        self._heading_object = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def project_area_code(self):
        return self._project_area_code

    @project_area_code.setter
    def project_area_code(self, value):
        self._project_area_code = value
    @property
    def project_area_desc(self):
        return self._project_area_desc

    @project_area_desc.setter
    def project_area_desc(self, value):
        self._project_area_desc = value
    @property
    def project_budget(self):
        return self._project_budget

    @project_budget.setter
    def project_budget(self, value):
        self._project_budget = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def text_object(self):
        return self._text_object

    @text_object.setter
    def text_object(self, value):
        self._text_object = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid_type:
            if hasattr(self.bid_type, 'to_alipay_dict'):
                params['bid_type'] = self.bid_type.to_alipay_dict()
            else:
                params['bid_type'] = self.bid_type
        if self.bidder_ep_cert_no:
            if hasattr(self.bidder_ep_cert_no, 'to_alipay_dict'):
                params['bidder_ep_cert_no'] = self.bidder_ep_cert_no.to_alipay_dict()
            else:
                params['bidder_ep_cert_no'] = self.bidder_ep_cert_no
        if self.bidder_ep_name:
            if hasattr(self.bidder_ep_name, 'to_alipay_dict'):
                params['bidder_ep_name'] = self.bidder_ep_name.to_alipay_dict()
            else:
                params['bidder_ep_name'] = self.bidder_ep_name
        if self.bidding_ep_cert_no:
            if hasattr(self.bidding_ep_cert_no, 'to_alipay_dict'):
                params['bidding_ep_cert_no'] = self.bidding_ep_cert_no.to_alipay_dict()
            else:
                params['bidding_ep_cert_no'] = self.bidding_ep_cert_no
        if self.bidding_ep_name:
            if hasattr(self.bidding_ep_name, 'to_alipay_dict'):
                params['bidding_ep_name'] = self.bidding_ep_name.to_alipay_dict()
            else:
                params['bidding_ep_name'] = self.bidding_ep_name
        if self.heading_object:
            if hasattr(self.heading_object, 'to_alipay_dict'):
                params['heading_object'] = self.heading_object.to_alipay_dict()
            else:
                params['heading_object'] = self.heading_object
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.project_area_code:
            if hasattr(self.project_area_code, 'to_alipay_dict'):
                params['project_area_code'] = self.project_area_code.to_alipay_dict()
            else:
                params['project_area_code'] = self.project_area_code
        if self.project_area_desc:
            if hasattr(self.project_area_desc, 'to_alipay_dict'):
                params['project_area_desc'] = self.project_area_desc.to_alipay_dict()
            else:
                params['project_area_desc'] = self.project_area_desc
        if self.project_budget:
            if hasattr(self.project_budget, 'to_alipay_dict'):
                params['project_budget'] = self.project_budget.to_alipay_dict()
            else:
                params['project_budget'] = self.project_budget
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.text_object:
            if hasattr(self.text_object, 'to_alipay_dict'):
                params['text_object'] = self.text_object.to_alipay_dict()
            else:
                params['text_object'] = self.text_object
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpZtbReportCreateModel()
        if 'bid_type' in d:
            o.bid_type = d['bid_type']
        if 'bidder_ep_cert_no' in d:
            o.bidder_ep_cert_no = d['bidder_ep_cert_no']
        if 'bidder_ep_name' in d:
            o.bidder_ep_name = d['bidder_ep_name']
        if 'bidding_ep_cert_no' in d:
            o.bidding_ep_cert_no = d['bidding_ep_cert_no']
        if 'bidding_ep_name' in d:
            o.bidding_ep_name = d['bidding_ep_name']
        if 'heading_object' in d:
            o.heading_object = d['heading_object']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'project_area_code' in d:
            o.project_area_code = d['project_area_code']
        if 'project_area_desc' in d:
            o.project_area_desc = d['project_area_desc']
        if 'project_budget' in d:
            o.project_budget = d['project_budget']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'text_object' in d:
            o.text_object = d['text_object']
        return o


