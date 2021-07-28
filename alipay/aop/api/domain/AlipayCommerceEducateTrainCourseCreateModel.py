#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CateInfo import CateInfo
from alipay.aop.api.domain.ShopMerchantInfo import ShopMerchantInfo
from alipay.aop.api.domain.CourseSKUInfo import CourseSKUInfo
from alipay.aop.api.domain.CourseTagInfo import CourseTagInfo


class AlipayCommerceEducateTrainCourseCreateModel(object):

    def __init__(self):
        self._biz_type = None
        self._brief = None
        self._cate_infos = None
        self._desc = None
        self._merchant_info = None
        self._name = None
        self._open_time = None
        self._out_course_id = None
        self._pic = None
        self._scene_type = None
        self._sku_infos = None
        self._source_type = None
        self._tag_infos = None
        self._url = None
        self._video = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def brief(self):
        return self._brief

    @brief.setter
    def brief(self, value):
        self._brief = value
    @property
    def cate_infos(self):
        return self._cate_infos

    @cate_infos.setter
    def cate_infos(self, value):
        if isinstance(value, list):
            self._cate_infos = list()
            for i in value:
                if isinstance(i, CateInfo):
                    self._cate_infos.append(i)
                else:
                    self._cate_infos.append(CateInfo.from_alipay_dict(i))
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, ShopMerchantInfo):
            self._merchant_info = value
        else:
            self._merchant_info = ShopMerchantInfo.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def out_course_id(self):
        return self._out_course_id

    @out_course_id.setter
    def out_course_id(self, value):
        self._out_course_id = value
    @property
    def pic(self):
        return self._pic

    @pic.setter
    def pic(self, value):
        self._pic = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def sku_infos(self):
        return self._sku_infos

    @sku_infos.setter
    def sku_infos(self, value):
        if isinstance(value, list):
            self._sku_infos = list()
            for i in value:
                if isinstance(i, CourseSKUInfo):
                    self._sku_infos.append(i)
                else:
                    self._sku_infos.append(CourseSKUInfo.from_alipay_dict(i))
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def tag_infos(self):
        return self._tag_infos

    @tag_infos.setter
    def tag_infos(self, value):
        if isinstance(value, list):
            self._tag_infos = list()
            for i in value:
                if isinstance(i, CourseTagInfo):
                    self._tag_infos.append(i)
                else:
                    self._tag_infos.append(CourseTagInfo.from_alipay_dict(i))
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def video(self):
        return self._video

    @video.setter
    def video(self, value):
        self._video = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.brief:
            if hasattr(self.brief, 'to_alipay_dict'):
                params['brief'] = self.brief.to_alipay_dict()
            else:
                params['brief'] = self.brief
        if self.cate_infos:
            if isinstance(self.cate_infos, list):
                for i in range(0, len(self.cate_infos)):
                    element = self.cate_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cate_infos[i] = element.to_alipay_dict()
            if hasattr(self.cate_infos, 'to_alipay_dict'):
                params['cate_infos'] = self.cate_infos.to_alipay_dict()
            else:
                params['cate_infos'] = self.cate_infos
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_time:
            if hasattr(self.open_time, 'to_alipay_dict'):
                params['open_time'] = self.open_time.to_alipay_dict()
            else:
                params['open_time'] = self.open_time
        if self.out_course_id:
            if hasattr(self.out_course_id, 'to_alipay_dict'):
                params['out_course_id'] = self.out_course_id.to_alipay_dict()
            else:
                params['out_course_id'] = self.out_course_id
        if self.pic:
            if hasattr(self.pic, 'to_alipay_dict'):
                params['pic'] = self.pic.to_alipay_dict()
            else:
                params['pic'] = self.pic
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.sku_infos:
            if isinstance(self.sku_infos, list):
                for i in range(0, len(self.sku_infos)):
                    element = self.sku_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_infos[i] = element.to_alipay_dict()
            if hasattr(self.sku_infos, 'to_alipay_dict'):
                params['sku_infos'] = self.sku_infos.to_alipay_dict()
            else:
                params['sku_infos'] = self.sku_infos
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.tag_infos:
            if isinstance(self.tag_infos, list):
                for i in range(0, len(self.tag_infos)):
                    element = self.tag_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_infos[i] = element.to_alipay_dict()
            if hasattr(self.tag_infos, 'to_alipay_dict'):
                params['tag_infos'] = self.tag_infos.to_alipay_dict()
            else:
                params['tag_infos'] = self.tag_infos
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.video:
            if hasattr(self.video, 'to_alipay_dict'):
                params['video'] = self.video.to_alipay_dict()
            else:
                params['video'] = self.video
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateTrainCourseCreateModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'brief' in d:
            o.brief = d['brief']
        if 'cate_infos' in d:
            o.cate_infos = d['cate_infos']
        if 'desc' in d:
            o.desc = d['desc']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'name' in d:
            o.name = d['name']
        if 'open_time' in d:
            o.open_time = d['open_time']
        if 'out_course_id' in d:
            o.out_course_id = d['out_course_id']
        if 'pic' in d:
            o.pic = d['pic']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'sku_infos' in d:
            o.sku_infos = d['sku_infos']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'tag_infos' in d:
            o.tag_infos = d['tag_infos']
        if 'url' in d:
            o.url = d['url']
        if 'video' in d:
            o.video = d['video']
        return o


