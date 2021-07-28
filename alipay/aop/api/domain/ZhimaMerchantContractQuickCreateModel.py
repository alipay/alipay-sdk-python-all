#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantContractQuickCreateModel(object):

    def __init__(self):
        self._category_code = None
        self._contract_content = None
        self._contract_principal_desc = None
        self._contract_principal_logo = None
        self._coupon_flag = None
        self._ext_info = None
        self._fufilment_callback_url = None
        self._fufilment_cnt = None
        self._fufilment_desc = None
        self._fufilment_end_time = None
        self._fufilment_period_type = None
        self._fufilment_start_time = None
        self._offer_creater_id = None
        self._offer_creater_name = None
        self._offer_creater_type = None
        self._out_biz_no = None
        self._out_content_name = None
        self._out_content_no = None
        self._service_id = None
        self._template_no = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def contract_content(self):
        return self._contract_content

    @contract_content.setter
    def contract_content(self, value):
        self._contract_content = value
    @property
    def contract_principal_desc(self):
        return self._contract_principal_desc

    @contract_principal_desc.setter
    def contract_principal_desc(self, value):
        self._contract_principal_desc = value
    @property
    def contract_principal_logo(self):
        return self._contract_principal_logo

    @contract_principal_logo.setter
    def contract_principal_logo(self, value):
        self._contract_principal_logo = value
    @property
    def coupon_flag(self):
        return self._coupon_flag

    @coupon_flag.setter
    def coupon_flag(self, value):
        self._coupon_flag = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fufilment_callback_url(self):
        return self._fufilment_callback_url

    @fufilment_callback_url.setter
    def fufilment_callback_url(self, value):
        self._fufilment_callback_url = value
    @property
    def fufilment_cnt(self):
        return self._fufilment_cnt

    @fufilment_cnt.setter
    def fufilment_cnt(self, value):
        self._fufilment_cnt = value
    @property
    def fufilment_desc(self):
        return self._fufilment_desc

    @fufilment_desc.setter
    def fufilment_desc(self, value):
        self._fufilment_desc = value
    @property
    def fufilment_end_time(self):
        return self._fufilment_end_time

    @fufilment_end_time.setter
    def fufilment_end_time(self, value):
        self._fufilment_end_time = value
    @property
    def fufilment_period_type(self):
        return self._fufilment_period_type

    @fufilment_period_type.setter
    def fufilment_period_type(self, value):
        self._fufilment_period_type = value
    @property
    def fufilment_start_time(self):
        return self._fufilment_start_time

    @fufilment_start_time.setter
    def fufilment_start_time(self, value):
        self._fufilment_start_time = value
    @property
    def offer_creater_id(self):
        return self._offer_creater_id

    @offer_creater_id.setter
    def offer_creater_id(self, value):
        self._offer_creater_id = value
    @property
    def offer_creater_name(self):
        return self._offer_creater_name

    @offer_creater_name.setter
    def offer_creater_name(self, value):
        self._offer_creater_name = value
    @property
    def offer_creater_type(self):
        return self._offer_creater_type

    @offer_creater_type.setter
    def offer_creater_type(self, value):
        self._offer_creater_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_content_name(self):
        return self._out_content_name

    @out_content_name.setter
    def out_content_name(self, value):
        self._out_content_name = value
    @property
    def out_content_no(self):
        return self._out_content_no

    @out_content_no.setter
    def out_content_no(self, value):
        self._out_content_no = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def template_no(self):
        return self._template_no

    @template_no.setter
    def template_no(self, value):
        self._template_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.contract_content:
            if hasattr(self.contract_content, 'to_alipay_dict'):
                params['contract_content'] = self.contract_content.to_alipay_dict()
            else:
                params['contract_content'] = self.contract_content
        if self.contract_principal_desc:
            if hasattr(self.contract_principal_desc, 'to_alipay_dict'):
                params['contract_principal_desc'] = self.contract_principal_desc.to_alipay_dict()
            else:
                params['contract_principal_desc'] = self.contract_principal_desc
        if self.contract_principal_logo:
            if hasattr(self.contract_principal_logo, 'to_alipay_dict'):
                params['contract_principal_logo'] = self.contract_principal_logo.to_alipay_dict()
            else:
                params['contract_principal_logo'] = self.contract_principal_logo
        if self.coupon_flag:
            if hasattr(self.coupon_flag, 'to_alipay_dict'):
                params['coupon_flag'] = self.coupon_flag.to_alipay_dict()
            else:
                params['coupon_flag'] = self.coupon_flag
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fufilment_callback_url:
            if hasattr(self.fufilment_callback_url, 'to_alipay_dict'):
                params['fufilment_callback_url'] = self.fufilment_callback_url.to_alipay_dict()
            else:
                params['fufilment_callback_url'] = self.fufilment_callback_url
        if self.fufilment_cnt:
            if hasattr(self.fufilment_cnt, 'to_alipay_dict'):
                params['fufilment_cnt'] = self.fufilment_cnt.to_alipay_dict()
            else:
                params['fufilment_cnt'] = self.fufilment_cnt
        if self.fufilment_desc:
            if hasattr(self.fufilment_desc, 'to_alipay_dict'):
                params['fufilment_desc'] = self.fufilment_desc.to_alipay_dict()
            else:
                params['fufilment_desc'] = self.fufilment_desc
        if self.fufilment_end_time:
            if hasattr(self.fufilment_end_time, 'to_alipay_dict'):
                params['fufilment_end_time'] = self.fufilment_end_time.to_alipay_dict()
            else:
                params['fufilment_end_time'] = self.fufilment_end_time
        if self.fufilment_period_type:
            if hasattr(self.fufilment_period_type, 'to_alipay_dict'):
                params['fufilment_period_type'] = self.fufilment_period_type.to_alipay_dict()
            else:
                params['fufilment_period_type'] = self.fufilment_period_type
        if self.fufilment_start_time:
            if hasattr(self.fufilment_start_time, 'to_alipay_dict'):
                params['fufilment_start_time'] = self.fufilment_start_time.to_alipay_dict()
            else:
                params['fufilment_start_time'] = self.fufilment_start_time
        if self.offer_creater_id:
            if hasattr(self.offer_creater_id, 'to_alipay_dict'):
                params['offer_creater_id'] = self.offer_creater_id.to_alipay_dict()
            else:
                params['offer_creater_id'] = self.offer_creater_id
        if self.offer_creater_name:
            if hasattr(self.offer_creater_name, 'to_alipay_dict'):
                params['offer_creater_name'] = self.offer_creater_name.to_alipay_dict()
            else:
                params['offer_creater_name'] = self.offer_creater_name
        if self.offer_creater_type:
            if hasattr(self.offer_creater_type, 'to_alipay_dict'):
                params['offer_creater_type'] = self.offer_creater_type.to_alipay_dict()
            else:
                params['offer_creater_type'] = self.offer_creater_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_content_name:
            if hasattr(self.out_content_name, 'to_alipay_dict'):
                params['out_content_name'] = self.out_content_name.to_alipay_dict()
            else:
                params['out_content_name'] = self.out_content_name
        if self.out_content_no:
            if hasattr(self.out_content_no, 'to_alipay_dict'):
                params['out_content_no'] = self.out_content_no.to_alipay_dict()
            else:
                params['out_content_no'] = self.out_content_no
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.template_no:
            if hasattr(self.template_no, 'to_alipay_dict'):
                params['template_no'] = self.template_no.to_alipay_dict()
            else:
                params['template_no'] = self.template_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantContractQuickCreateModel()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'contract_content' in d:
            o.contract_content = d['contract_content']
        if 'contract_principal_desc' in d:
            o.contract_principal_desc = d['contract_principal_desc']
        if 'contract_principal_logo' in d:
            o.contract_principal_logo = d['contract_principal_logo']
        if 'coupon_flag' in d:
            o.coupon_flag = d['coupon_flag']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fufilment_callback_url' in d:
            o.fufilment_callback_url = d['fufilment_callback_url']
        if 'fufilment_cnt' in d:
            o.fufilment_cnt = d['fufilment_cnt']
        if 'fufilment_desc' in d:
            o.fufilment_desc = d['fufilment_desc']
        if 'fufilment_end_time' in d:
            o.fufilment_end_time = d['fufilment_end_time']
        if 'fufilment_period_type' in d:
            o.fufilment_period_type = d['fufilment_period_type']
        if 'fufilment_start_time' in d:
            o.fufilment_start_time = d['fufilment_start_time']
        if 'offer_creater_id' in d:
            o.offer_creater_id = d['offer_creater_id']
        if 'offer_creater_name' in d:
            o.offer_creater_name = d['offer_creater_name']
        if 'offer_creater_type' in d:
            o.offer_creater_type = d['offer_creater_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_content_name' in d:
            o.out_content_name = d['out_content_name']
        if 'out_content_no' in d:
            o.out_content_no = d['out_content_no']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'template_no' in d:
            o.template_no = d['template_no']
        return o


