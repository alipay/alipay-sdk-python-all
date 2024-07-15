#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CouponMsgVO import CouponMsgVO
from alipay.aop.api.domain.ImageMsgVO import ImageMsgVO
from alipay.aop.api.domain.LinkMsgVO import LinkMsgVO
from alipay.aop.api.domain.TextMsgVO import TextMsgVO
from alipay.aop.api.domain.TinyAppMsgVO import TinyAppMsgVO


class GroupMessageVO(object):

    def __init__(self):
        self._coupon_msg_content = None
        self._image_msg_content = None
        self._link_msg_content = None
        self._msg_type = None
        self._text_msg_content = None
        self._tiny_app_msg_content = None

    @property
    def coupon_msg_content(self):
        return self._coupon_msg_content

    @coupon_msg_content.setter
    def coupon_msg_content(self, value):
        if isinstance(value, CouponMsgVO):
            self._coupon_msg_content = value
        else:
            self._coupon_msg_content = CouponMsgVO.from_alipay_dict(value)
    @property
    def image_msg_content(self):
        return self._image_msg_content

    @image_msg_content.setter
    def image_msg_content(self, value):
        if isinstance(value, ImageMsgVO):
            self._image_msg_content = value
        else:
            self._image_msg_content = ImageMsgVO.from_alipay_dict(value)
    @property
    def link_msg_content(self):
        return self._link_msg_content

    @link_msg_content.setter
    def link_msg_content(self, value):
        if isinstance(value, LinkMsgVO):
            self._link_msg_content = value
        else:
            self._link_msg_content = LinkMsgVO.from_alipay_dict(value)
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def text_msg_content(self):
        return self._text_msg_content

    @text_msg_content.setter
    def text_msg_content(self, value):
        if isinstance(value, TextMsgVO):
            self._text_msg_content = value
        else:
            self._text_msg_content = TextMsgVO.from_alipay_dict(value)
    @property
    def tiny_app_msg_content(self):
        return self._tiny_app_msg_content

    @tiny_app_msg_content.setter
    def tiny_app_msg_content(self, value):
        if isinstance(value, TinyAppMsgVO):
            self._tiny_app_msg_content = value
        else:
            self._tiny_app_msg_content = TinyAppMsgVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.coupon_msg_content:
            if hasattr(self.coupon_msg_content, 'to_alipay_dict'):
                params['coupon_msg_content'] = self.coupon_msg_content.to_alipay_dict()
            else:
                params['coupon_msg_content'] = self.coupon_msg_content
        if self.image_msg_content:
            if hasattr(self.image_msg_content, 'to_alipay_dict'):
                params['image_msg_content'] = self.image_msg_content.to_alipay_dict()
            else:
                params['image_msg_content'] = self.image_msg_content
        if self.link_msg_content:
            if hasattr(self.link_msg_content, 'to_alipay_dict'):
                params['link_msg_content'] = self.link_msg_content.to_alipay_dict()
            else:
                params['link_msg_content'] = self.link_msg_content
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        if self.text_msg_content:
            if hasattr(self.text_msg_content, 'to_alipay_dict'):
                params['text_msg_content'] = self.text_msg_content.to_alipay_dict()
            else:
                params['text_msg_content'] = self.text_msg_content
        if self.tiny_app_msg_content:
            if hasattr(self.tiny_app_msg_content, 'to_alipay_dict'):
                params['tiny_app_msg_content'] = self.tiny_app_msg_content.to_alipay_dict()
            else:
                params['tiny_app_msg_content'] = self.tiny_app_msg_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupMessageVO()
        if 'coupon_msg_content' in d:
            o.coupon_msg_content = d['coupon_msg_content']
        if 'image_msg_content' in d:
            o.image_msg_content = d['image_msg_content']
        if 'link_msg_content' in d:
            o.link_msg_content = d['link_msg_content']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        if 'text_msg_content' in d:
            o.text_msg_content = d['text_msg_content']
        if 'tiny_app_msg_content' in d:
            o.tiny_app_msg_content = d['tiny_app_msg_content']
        return o


