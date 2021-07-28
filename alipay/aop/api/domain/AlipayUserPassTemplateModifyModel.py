#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TemplateEvoucherDTO import TemplateEvoucherDTO
from alipay.aop.api.domain.TemplateFileDTO import TemplateFileDTO
from alipay.aop.api.domain.TemplateImageDTO import TemplateImageDTO
from alipay.aop.api.domain.TemplateMerchantDTO import TemplateMerchantDTO
from alipay.aop.api.domain.TemplatePlatformDTO import TemplatePlatformDTO
from alipay.aop.api.domain.TemplateStyleDTO import TemplateStyleDTO


class AlipayUserPassTemplateModifyModel(object):

    def __init__(self):
        self._evoucher_info = None
        self._file_info = None
        self._image = None
        self._merchant = None
        self._platform = None
        self._style = None
        self._template_id = None

    @property
    def evoucher_info(self):
        return self._evoucher_info

    @evoucher_info.setter
    def evoucher_info(self, value):
        if isinstance(value, TemplateEvoucherDTO):
            self._evoucher_info = value
        else:
            self._evoucher_info = TemplateEvoucherDTO.from_alipay_dict(value)
    @property
    def file_info(self):
        return self._file_info

    @file_info.setter
    def file_info(self, value):
        if isinstance(value, TemplateFileDTO):
            self._file_info = value
        else:
            self._file_info = TemplateFileDTO.from_alipay_dict(value)
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        if isinstance(value, TemplateImageDTO):
            self._image = value
        else:
            self._image = TemplateImageDTO.from_alipay_dict(value)
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, TemplateMerchantDTO):
            self._merchant = value
        else:
            self._merchant = TemplateMerchantDTO.from_alipay_dict(value)
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        if isinstance(value, TemplatePlatformDTO):
            self._platform = value
        else:
            self._platform = TemplatePlatformDTO.from_alipay_dict(value)
    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        if isinstance(value, TemplateStyleDTO):
            self._style = value
        else:
            self._style = TemplateStyleDTO.from_alipay_dict(value)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.evoucher_info:
            if hasattr(self.evoucher_info, 'to_alipay_dict'):
                params['evoucher_info'] = self.evoucher_info.to_alipay_dict()
            else:
                params['evoucher_info'] = self.evoucher_info
        if self.file_info:
            if hasattr(self.file_info, 'to_alipay_dict'):
                params['file_info'] = self.file_info.to_alipay_dict()
            else:
                params['file_info'] = self.file_info
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.style:
            if hasattr(self.style, 'to_alipay_dict'):
                params['style'] = self.style.to_alipay_dict()
            else:
                params['style'] = self.style
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPassTemplateModifyModel()
        if 'evoucher_info' in d:
            o.evoucher_info = d['evoucher_info']
        if 'file_info' in d:
            o.file_info = d['file_info']
        if 'image' in d:
            o.image = d['image']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'platform' in d:
            o.platform = d['platform']
        if 'style' in d:
            o.style = d['style']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


