#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlgorithmGoodsInfo(object):

    def __init__(self):
        self._algorithm_goods_id = None
        self._gif_file_id = None
        self._pic_file_id = None
        self._three_dimension = None
        self._thumbnails = None

    @property
    def algorithm_goods_id(self):
        return self._algorithm_goods_id

    @algorithm_goods_id.setter
    def algorithm_goods_id(self, value):
        self._algorithm_goods_id = value
    @property
    def gif_file_id(self):
        return self._gif_file_id

    @gif_file_id.setter
    def gif_file_id(self, value):
        self._gif_file_id = value
    @property
    def pic_file_id(self):
        return self._pic_file_id

    @pic_file_id.setter
    def pic_file_id(self, value):
        self._pic_file_id = value
    @property
    def three_dimension(self):
        return self._three_dimension

    @three_dimension.setter
    def three_dimension(self, value):
        self._three_dimension = value
    @property
    def thumbnails(self):
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, value):
        self._thumbnails = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_goods_id:
            if hasattr(self.algorithm_goods_id, 'to_alipay_dict'):
                params['algorithm_goods_id'] = self.algorithm_goods_id.to_alipay_dict()
            else:
                params['algorithm_goods_id'] = self.algorithm_goods_id
        if self.gif_file_id:
            if hasattr(self.gif_file_id, 'to_alipay_dict'):
                params['gif_file_id'] = self.gif_file_id.to_alipay_dict()
            else:
                params['gif_file_id'] = self.gif_file_id
        if self.pic_file_id:
            if hasattr(self.pic_file_id, 'to_alipay_dict'):
                params['pic_file_id'] = self.pic_file_id.to_alipay_dict()
            else:
                params['pic_file_id'] = self.pic_file_id
        if self.three_dimension:
            if hasattr(self.three_dimension, 'to_alipay_dict'):
                params['three_dimension'] = self.three_dimension.to_alipay_dict()
            else:
                params['three_dimension'] = self.three_dimension
        if self.thumbnails:
            if hasattr(self.thumbnails, 'to_alipay_dict'):
                params['thumbnails'] = self.thumbnails.to_alipay_dict()
            else:
                params['thumbnails'] = self.thumbnails
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlgorithmGoodsInfo()
        if 'algorithm_goods_id' in d:
            o.algorithm_goods_id = d['algorithm_goods_id']
        if 'gif_file_id' in d:
            o.gif_file_id = d['gif_file_id']
        if 'pic_file_id' in d:
            o.pic_file_id = d['pic_file_id']
        if 'three_dimension' in d:
            o.three_dimension = d['three_dimension']
        if 'thumbnails' in d:
            o.thumbnails = d['thumbnails']
        return o


