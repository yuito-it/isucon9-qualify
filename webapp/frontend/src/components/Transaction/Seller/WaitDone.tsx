import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Typography } from '@material-ui/core';

const useStyles = makeStyles(theme => ({}));

type Props = {};

const WaitDone: React.FC<Props> = () => {
  const classes = useStyles();

  return (
    <React.Fragment>
      <Typography variant="h6">商品を発送しました</Typography>
      <Typography variant="h6">
        購入者が商品を受け取るのをお待ち下さい
      </Typography>
    </React.Fragment>
  );
};

export default WaitDone;
