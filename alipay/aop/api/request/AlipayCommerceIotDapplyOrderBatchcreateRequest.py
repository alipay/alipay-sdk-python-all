#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayCommerceIotDapplyOrderBatchcreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._applicant_mobile = None
        self._applicant_name = None
        self._channel_code = None
        self._item_id = None
        self._mall_item_id = None
        self._memo = None
        self._out_biz_no = None
        self._source_code = None
        self._support_mall_item_id = None
        self._total_apply_amount = None
        self._total_apply_count = None
        self._usb_mall_item_id = None
        self._file_content = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def applicant_mobile(self):
        return self._applicant_mobile

    @applicant_mobile.setter
    def applicant_mobile(self, value):
        self._applicant_mobile = value
    @property
    def applicant_name(self):
        return self._applicant_name

    @applicant_name.setter
    def applicant_name(self, value):
        self._applicant_name = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mall_item_id(self):
        return self._mall_item_id

    @mall_item_id.setter
    def mall_item_id(self, value):
        self._mall_item_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source_code(self):
        return self._source_code

    @source_code.setter
    def source_code(self, value):
        self._source_code = value
    @property
    def support_mall_item_id(self):
        return self._support_mall_item_id

    @support_mall_item_id.setter
    def support_mall_item_id(self, value):
        self._support_mall_item_id = value
    @property
    def total_apply_amount(self):
        return self._total_apply_amount

    @total_apply_amount.setter
    def total_apply_amount(self, value):
        self._total_apply_amount = value
    @property
    def total_apply_count(self):
        return self._total_apply_count

    @total_apply_count.setter
    def total_apply_count(self, value):
        self._total_apply_count = value
    @property
    def usb_mall_item_id(self):
        return self._usb_mall_item_id

    @usb_mall_item_id.setter
    def usb_mall_item_id(self, value):
        self._usb_mall_item_id = value

    @property
    def file_content(self):
        return self._file_content

    @file_content.setter
    def file_content(self, value):
        if not isinstance(value, FileItem):
            return
        self._file_content = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.commerce.iot.dapply.order.batchcreate'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.applicant_mobile:
            if hasattr(self.applicant_mobile, 'to_alipay_dict'):
                params['applicant_mobile'] = json.dumps(obj=self.applicant_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['applicant_mobile'] = self.applicant_mobile
        if self.applicant_name:
            if hasattr(self.applicant_name, 'to_alipay_dict'):
                params['applicant_name'] = json.dumps(obj=self.applicant_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['applicant_name'] = self.applicant_name
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = json.dumps(obj=self.channel_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['channel_code'] = self.channel_code
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = json.dumps(obj=self.item_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['item_id'] = self.item_id
        if self.mall_item_id:
            if hasattr(self.mall_item_id, 'to_alipay_dict'):
                params['mall_item_id'] = json.dumps(obj=self.mall_item_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mall_item_id'] = self.mall_item_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = json.dumps(obj=self.memo.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['memo'] = self.memo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = json.dumps(obj=self.out_biz_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source_code:
            if hasattr(self.source_code, 'to_alipay_dict'):
                params['source_code'] = json.dumps(obj=self.source_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['source_code'] = self.source_code
        if self.support_mall_item_id:
            if hasattr(self.support_mall_item_id, 'to_alipay_dict'):
                params['support_mall_item_id'] = json.dumps(obj=self.support_mall_item_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['support_mall_item_id'] = self.support_mall_item_id
        if self.total_apply_amount:
            if hasattr(self.total_apply_amount, 'to_alipay_dict'):
                params['total_apply_amount'] = json.dumps(obj=self.total_apply_amount.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['total_apply_amount'] = self.total_apply_amount
        if self.total_apply_count:
            if hasattr(self.total_apply_count, 'to_alipay_dict'):
                params['total_apply_count'] = json.dumps(obj=self.total_apply_count.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['total_apply_count'] = self.total_apply_count
        if self.usb_mall_item_id:
            if hasattr(self.usb_mall_item_id, 'to_alipay_dict'):
                params['usb_mall_item_id'] = json.dumps(obj=self.usb_mall_item_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['usb_mall_item_id'] = self.usb_mall_item_id
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.file_content:
            multipart_params['file_content'] = self.file_content
        return multipart_params
