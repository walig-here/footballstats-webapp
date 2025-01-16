import {test, expect} from 'vitest'
import {render, screen} from '@testing-library/react'

import { LoadingView } from "../../../src/views/utilities/LoadingView.jsx";


test('LoadingView -> when rendered then headline visible', () => {
    render(<LoadingView/>);

    expect(screen.getByTestId('headline')).toBeInTheDocument();
});

test('LoadingView -> when rendered then loading circle visible', () => {
    render(<LoadingView/>);

    expect(screen.getByTestId('loading-circle')).toBeInTheDocument();
})