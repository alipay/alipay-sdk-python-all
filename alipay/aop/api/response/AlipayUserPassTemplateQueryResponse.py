#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TemplateEvoucherDTO import TemplateEvoucherDTO
from alipay.aop.api.domain.TemplateFileDTO import TemplateFileDTO
from alipay.aop.api.domain.TemplateImageDTO import TemplateImageDTO
from alipay.aop.api.domain.TemplateMerchantDTO import TemplateMerchantDTO
from alipay.aop.api.domain.TemplatePlatformDTO import TemplatePlatformDTO
from alipay.aop.api.domain.TemplateStyleDTO import TemplateStyleDTO


class AlipayUserPassTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserPassTemplateQueryResponse, self).__init__()
        self._evoucher_info = None
        self._file_info = None
        self._image = None
        self._merchant = None
        self._platform = None
        self._style = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayUserPassTemplateQueryResponse, self).parse_response_content(response_content)
        if 'evoucher_info' in response:
            self.evoucher_info = response['evoucher_info']
        if 'file_info' in response:
            self.file_info = response['file_info']
        if 'image' in response:
            self.image = response['image']
        if 'merchant' in response:
            self.merchant = response['merchant']
        if 'platform' in response:
            self.platform = response['platform']
        if 'style' in response:
            self.style = response['style']
