#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoAgreementInfo import PromoAgreementInfo


class AlipayMerchantNpromoIndirectQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantNpromoIndirectQueryResponse, self).__init__()
        self._pop_agreement_desc = None
        self._pop_agreement_list = None
        self._pop_body_img = None
        self._pop_brand_img = None
        self._pop_btn_img = None
        self._pop_header_img = None
        self._pop_url = None
        self._remark = None
        self._scene = None
        self._show = None

    @property
    def pop_agreement_desc(self):
        return self._pop_agreement_desc

    @pop_agreement_desc.setter
    def pop_agreement_desc(self, value):
        self._pop_agreement_desc = value
    @property
    def pop_agreement_list(self):
        return self._pop_agreement_list

    @pop_agreement_list.setter
    def pop_agreement_list(self, value):
        if isinstance(value, list):
            self._pop_agreement_list = list()
            for i in value:
                if isinstance(i, PromoAgreementInfo):
                    self._pop_agreement_list.append(i)
                else:
                    self._pop_agreement_list.append(PromoAgreementInfo.from_alipay_dict(i))
    @property
    def pop_body_img(self):
        return self._pop_body_img

    @pop_body_img.setter
    def pop_body_img(self, value):
        self._pop_body_img = value
    @property
    def pop_brand_img(self):
        return self._pop_brand_img

    @pop_brand_img.setter
    def pop_brand_img(self, value):
        self._pop_brand_img = value
    @property
    def pop_btn_img(self):
        return self._pop_btn_img

    @pop_btn_img.setter
    def pop_btn_img(self, value):
        self._pop_btn_img = value
    @property
    def pop_header_img(self):
        return self._pop_header_img

    @pop_header_img.setter
    def pop_header_img(self, value):
        self._pop_header_img = value
    @property
    def pop_url(self):
        return self._pop_url

    @pop_url.setter
    def pop_url(self, value):
        self._pop_url = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, value):
        self._show = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantNpromoIndirectQueryResponse, self).parse_response_content(response_content)
        if 'pop_agreement_desc' in response:
            self.pop_agreement_desc = response['pop_agreement_desc']
        if 'pop_agreement_list' in response:
            self.pop_agreement_list = response['pop_agreement_list']
        if 'pop_body_img' in response:
            self.pop_body_img = response['pop_body_img']
        if 'pop_brand_img' in response:
            self.pop_brand_img = response['pop_brand_img']
        if 'pop_btn_img' in response:
            self.pop_btn_img = response['pop_btn_img']
        if 'pop_header_img' in response:
            self.pop_header_img = response['pop_header_img']
        if 'pop_url' in response:
            self.pop_url = response['pop_url']
        if 'remark' in response:
            self.remark = response['remark']
        if 'scene' in response:
            self.scene = response['scene']
        if 'show' in response:
            self.show = response['show']
